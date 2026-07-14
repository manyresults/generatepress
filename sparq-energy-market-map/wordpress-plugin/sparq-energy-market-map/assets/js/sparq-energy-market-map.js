/*
 * SPARQ Energy Market Map — behaviour
 *
 * Renders an interactive US map with jsVectorMap and lets the visitor toggle
 * between two energy markets (Electricity retail choice / Natural Gas customer
 * choice). Each state is coloured by how open its retail market is, and the
 * side panel + tooltips update to match the selected market.
 *
 * Requires (loaded before this file):
 *   - jsvectormap.min.js   (the library, exposes window.jsVectorMap)
 *   - us-aea.js            (registers the "us_aea" US-states map)
 */
(function () {
  "use strict";

  var colors = {
    regulated: "#d9dee7",
    full: "#c9a227",
    limited: "#6f8faa",
    stroke: "#ffffff"
  };

  // jsVectorMap "ordinal" scale: maps a status category -> fill colour.
  // Regions are given a status (below); the series looks the colour up here.
  var scale = {
    full: colors.full,
    limited: colors.limited,
    regulated: colors.regulated
  };

  var stateNames = {
    "US-AL": "Alabama", "US-AK": "Alaska", "US-AZ": "Arizona", "US-AR": "Arkansas",
    "US-CA": "California", "US-CO": "Colorado", "US-CT": "Connecticut", "US-DE": "Delaware",
    "US-DC": "Washington, D.C.", "US-FL": "Florida", "US-GA": "Georgia", "US-HI": "Hawaii",
    "US-ID": "Idaho", "US-IL": "Illinois", "US-IN": "Indiana", "US-IA": "Iowa",
    "US-KS": "Kansas", "US-KY": "Kentucky", "US-LA": "Louisiana", "US-ME": "Maine",
    "US-MD": "Maryland", "US-MA": "Massachusetts", "US-MI": "Michigan", "US-MN": "Minnesota",
    "US-MS": "Mississippi", "US-MO": "Missouri", "US-MT": "Montana", "US-NE": "Nebraska",
    "US-NV": "Nevada", "US-NH": "New Hampshire", "US-NJ": "New Jersey", "US-NM": "New Mexico",
    "US-NY": "New York", "US-NC": "North Carolina", "US-ND": "North Dakota", "US-OH": "Ohio",
    "US-OK": "Oklahoma", "US-OR": "Oregon", "US-PA": "Pennsylvania", "US-RI": "Rhode Island",
    "US-SC": "South Carolina", "US-SD": "South Dakota", "US-TN": "Tennessee", "US-TX": "Texas",
    "US-UT": "Utah", "US-VT": "Vermont", "US-VA": "Virginia", "US-WA": "Washington",
    "US-WV": "West Virginia", "US-WI": "Wisconsin", "US-WY": "Wyoming"
  };

  /*
    IMPORTANT:
    These lists are a starting point for public education.
    Before publishing as service coverage, confirm with the SPARQ energy provider.
  */

  var marketData = {
    electricity: {
      title: "Electricity Retail Choice",
      description: "Some states allow electricity customers to choose a competitive supplier, while the local utility continues to deliver power and maintain the infrastructure.",
      fullLabel: "Deregulated / retail choice",
      limitedLabel: "Limited or utility-specific choice",
      full: [
        "US-CT", "US-DE", "US-DC", "US-IL", "US-ME", "US-MD", "US-MA",
        "US-NH", "US-NJ", "US-NY", "US-OH", "US-PA", "US-RI", "US-TX"
      ],
      limited: [
        "US-CA", "US-MI", "US-NV", "US-OR", "US-VA"
      ]
    },
    gas: {
      title: "Natural Gas Customer Choice",
      description: "Some states allow natural gas customers to purchase supply from an approved marketer while the local distribution utility continues to deliver the gas.",
      fullLabel: "Customer choice available",
      limitedLabel: "Limited, territory-specific, or low participation",
      full: [
        "US-CA", "US-CT", "US-DC", "US-FL", "US-GA", "US-IL", "US-IN", "US-KY",
        "US-MD", "US-MA", "US-MI", "US-MT", "US-NE", "US-NJ", "US-NM", "US-NY",
        "US-OH", "US-PA", "US-RI", "US-VA", "US-WI", "US-WY"
      ],
      limited: []
    }
  };

  var currentMarket = "electricity";
  var map;

  function getStatus(code, market) {
    var data = marketData[market];

    if (data.full.indexOf(code) !== -1) {
      return "full";
    }

    if (data.limited.indexOf(code) !== -1) {
      return "limited";
    }

    return "regulated";
  }

  // Map every state code -> its status ("full" | "limited" | "regulated").
  // The series' ordinal scale (above) turns each status into a fill colour.
  function buildRegionValues(market) {
    var values = {};
    Object.keys(stateNames).forEach(function (code) {
      values[code] = getStatus(code, market);
    });
    return values;
  }

  function statusText(status, market) {
    if (market === "gas") {
      if (status === "full") return "Customer choice available in some form";
      if (status === "limited") return "Limited or territory-specific choice";
      return "No broad residential customer choice identified";
    }

    if (status === "full") return "Deregulated / retail choice";
    if (status === "limited") return "Limited or utility-specific choice";
    return "Regulated / no broad retail choice";
  }

  function updateSidePanel(market) {
    var data = marketData[market];

    document.getElementById("sparq-market-title").textContent = data.title;
    document.getElementById("sparq-market-description").textContent = data.description;
    document.getElementById("sparq-full-label").textContent = data.fullLabel;
    document.getElementById("sparq-limited-label").textContent = data.limitedLabel;

    var fullStates = data.full.map(function (code) { return stateNames[code]; }).sort().join(", ");
    var limitedStates = data.limited.length
      ? data.limited.map(function (code) { return stateNames[code]; }).sort().join(", ")
      : "Eligibility varies by account and territory.";

    document.getElementById("sparq-state-list").innerHTML =
      "<p><strong>" + data.fullLabel + ":</strong><br>" + fullStates + "</p>" +
      "<p><strong>" + data.limitedLabel + ":</strong><br>" + limitedStates + "</p>";
  }

  function updateMap(market) {
    currentMarket = market;

    document.querySelectorAll("#sparq-energy-market-map .sparq-toggle").forEach(function (button) {
      button.classList.toggle("active", button.getAttribute("data-market") === market);
    });

    if (map && map.series && map.series.regions && map.series.regions[0]) {
      map.series.regions[0].setValues(buildRegionValues(market));
    }

    updateSidePanel(market);
  }

  function initMap() {
    if (!window.jsVectorMap) {
      console.warn("SPARQ energy map: jsVectorMap did not load.");
      return;
    }

    if (!document.getElementById("sparq-us-energy-map")) {
      return;
    }

    map = new window.jsVectorMap({
      selector: "#sparq-us-energy-map",
      map: "us_aea",
      zoomButtons: false,
      zoomOnScroll: false,
      regionStyle: {
        initial: {
          fill: colors.regulated,
          stroke: colors.stroke,
          strokeWidth: 1
        },
        hover: {
          fill: "#e2b844"
        }
      },
      series: {
        regions: [{
          attribute: "fill",
          scale: scale,
          values: buildRegionValues(currentMarket)
        }]
      },
      onRegionTooltipShow: function (event, tooltip, code) {
        var state = stateNames[code] || code;
        var status = getStatus(code, currentMarket);
        tooltip.text(state + ": " + statusText(status, currentMarket));
      }
    });

    updateSidePanel(currentMarket);

    document.querySelectorAll("#sparq-energy-market-map .sparq-toggle").forEach(function (button) {
      button.addEventListener("click", function () {
        updateMap(this.getAttribute("data-market"));
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initMap);
  } else {
    initMap();
  }
})();
