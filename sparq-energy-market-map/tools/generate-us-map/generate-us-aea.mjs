import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import * as topojson from 'topojson-client';
import { geoPath, geoIdentity } from 'd3-geo';

const HERE = dirname(fileURLToPath(import.meta.url));
const ATLAS = join(HERE, 'node_modules/us-atlas/states-albers-10m.json');
// Regenerated map lands directly in the standalone/demo vendor folder.
// After running this, re-sync the plugin copy (see project README).
const OUT = join(HERE, '../../assets/vendor/jsvectormap/us-aea.js');

// FIPS -> { code: USPS, name }. 50 states + DC.
const FIPS = {
  '01': ['AL', 'Alabama'], '02': ['AK', 'Alaska'], '04': ['AZ', 'Arizona'],
  '05': ['AR', 'Arkansas'], '06': ['CA', 'California'], '08': ['CO', 'Colorado'],
  '09': ['CT', 'Connecticut'], '10': ['DE', 'Delaware'], '11': ['DC', 'District of Columbia'],
  '12': ['FL', 'Florida'], '13': ['GA', 'Georgia'], '15': ['HI', 'Hawaii'],
  '16': ['ID', 'Idaho'], '17': ['IL', 'Illinois'], '18': ['IN', 'Indiana'],
  '19': ['IA', 'Iowa'], '20': ['KS', 'Kansas'], '21': ['KY', 'Kentucky'],
  '22': ['LA', 'Louisiana'], '23': ['ME', 'Maine'], '24': ['MD', 'Maryland'],
  '25': ['MA', 'Massachusetts'], '26': ['MI', 'Michigan'], '27': ['MN', 'Minnesota'],
  '28': ['MS', 'Mississippi'], '29': ['MO', 'Missouri'], '30': ['MT', 'Montana'],
  '31': ['NE', 'Nebraska'], '32': ['NV', 'Nevada'], '33': ['NH', 'New Hampshire'],
  '34': ['NJ', 'New Jersey'], '35': ['NM', 'New Mexico'], '36': ['NY', 'New York'],
  '37': ['NC', 'North Carolina'], '38': ['ND', 'North Dakota'], '39': ['OH', 'Ohio'],
  '40': ['OK', 'Oklahoma'], '41': ['OR', 'Oregon'], '42': ['PA', 'Pennsylvania'],
  '44': ['RI', 'Rhode Island'], '45': ['SC', 'South Carolina'], '46': ['SD', 'South Dakota'],
  '47': ['TN', 'Tennessee'], '48': ['TX', 'Texas'], '49': ['UT', 'Utah'],
  '50': ['VT', 'Vermont'], '51': ['VA', 'Virginia'], '53': ['WA', 'Washington'],
  '54': ['WV', 'West Virginia'], '55': ['WI', 'Wisconsin'], '56': ['WY', 'Wyoming'],
};

const TARGET_WIDTH = 900;

const topo = JSON.parse(readFileSync(ATLAS, 'utf8'));
const fc = topojson.feature(topo, topo.objects.states);

// Keep only the 50 states + DC, attach USPS code.
fc.features = fc.features.filter((f) => FIPS[String(f.id)]);
fc.features.forEach((f) => {
  const [code, name] = FIPS[String(f.id)];
  f._code = 'US-' + code;
  f._name = name;
});

// Coordinates are already in Albers-USA planar space (AK & HI inset). Use an
// identity transform: fit to the target width, then shift the bounds to (0,0).
const projection = geoIdentity();
projection.fitWidth(TARGET_WIDTH, fc);
let path = geoPath(projection);
const [[x0, y0], [x1, y1]] = path.bounds(fc);
const t = projection.translate();
projection.translate([t[0] - x0, t[1] - y0]);
path = geoPath(projection).digits ? geoPath(projection).digits(2) : geoPath(projection);

const width = Math.ceil(x1 - x0);
const height = Math.ceil(y1 - y0);

const round = (d) => d.replace(/-?\d+\.\d+/g, (n) => String(Math.round(parseFloat(n) * 100) / 100));

const paths = {};
fc.features
  .sort((a, b) => a._code.localeCompare(b._code))
  .forEach((f) => {
    const d = path(f);
    if (!d) {
      console.error('WARN: no path for', f._code);
      return;
    }
    paths[f._code] = { path: round(d), name: f._name };
  });

const mapData = {
  insets: [
    { width, top: 0, left: 0, height, bbox: [{ x: 0, y: 0 }, { x: width, y: height }] },
  ],
  paths,
  width,
  height,
};

const banner =
  '/*!\n' +
  ' * us_aea map for jsVectorMap (US states, Albers Equal-Area, AK & HI inset).\n' +
  ' * Generated from us-atlas states-albers-10m (Natural Earth, public domain)\n' +
  ' * via d3-geo. Registers under the name "us_aea".\n' +
  ' */\n';

const out =
  banner +
  '"use strict";\n' +
  '(function () {\n' +
  '  var register = function () {\n' +
  '    window.jsVectorMap.addMap("us_aea", ' +
  JSON.stringify(mapData) +
  ');\n' +
  '  };\n' +
  '  if (window.jsVectorMap) { register(); }\n' +
  '  else { window.addEventListener("DOMContentLoaded", register); }\n' +
  '})();\n';

writeFileSync(OUT, out);
console.log('Wrote', OUT);
console.log('states:', Object.keys(paths).length, '| width:', width, '| height:', height);
console.log('bytes:', out.length);
