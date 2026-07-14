<?php
/**
 * Plugin Name:       SPARQ Energy Market Map
 * Description:        Interactive US map of energy deregulation (electricity retail choice & natural gas customer choice). Add it anywhere with the [sparq_energy_market_map] shortcode.
 * Version:           1.0.0
 * Requires at least: 5.0
 * Requires PHP:      7.0
 * Author:            SPARQ / ManyResults
 * License:           MIT
 * Text Domain:       sparq-energy-market-map
 *
 * The map library (jsVectorMap) and the US-states map file are bundled with this
 * plugin under assets/vendor/ — nothing is loaded from a third-party CDN, so the
 * component keeps working even if an external CDN is blocked or offline.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // No direct access.
}

define( 'SPARQ_EMM_VERSION', '1.0.0' );
define( 'SPARQ_EMM_URL', plugin_dir_url( __FILE__ ) );
define( 'SPARQ_EMM_PATH', plugin_dir_path( __FILE__ ) );

/**
 * Register (but don't enqueue) all styles and scripts. They are enqueued on
 * demand by the shortcode so pages without the map stay lightweight.
 */
function sparq_emm_register_assets() {
	wp_register_style(
		'jsvectormap',
		SPARQ_EMM_URL . 'assets/vendor/jsvectormap/jsvectormap.min.css',
		array(),
		'1.6.0'
	);

	wp_register_style(
		'sparq-emm',
		SPARQ_EMM_URL . 'assets/css/sparq-energy-market-map.css',
		array( 'jsvectormap' ),
		SPARQ_EMM_VERSION
	);

	wp_register_script(
		'jsvectormap',
		SPARQ_EMM_URL . 'assets/vendor/jsvectormap/jsvectormap.min.js',
		array(),
		'1.6.0',
		true
	);

	// Registers the "us_aea" map on window.jsVectorMap. Depends on the library.
	wp_register_script(
		'jsvectormap-us-aea',
		SPARQ_EMM_URL . 'assets/vendor/jsvectormap/us-aea.js',
		array( 'jsvectormap' ),
		'1.6.0',
		true
	);

	wp_register_script(
		'sparq-emm',
		SPARQ_EMM_URL . 'assets/js/sparq-energy-market-map.js',
		array( 'jsvectormap', 'jsvectormap-us-aea' ),
		SPARQ_EMM_VERSION,
		true
	);
}
add_action( 'wp_enqueue_scripts', 'sparq_emm_register_assets' );

/**
 * [sparq_energy_market_map] shortcode.
 *
 * Attributes:
 *   review_url  — URL for the "Start Review" button (default: /start-review/)
 *   contact_url — URL for the "Contact Us" button  (default: /contact/)
 *
 * Example: [sparq_energy_market_map review_url="/energy-review/" contact_url="/contact/"]
 */
function sparq_emm_shortcode( $atts ) {
	$atts = shortcode_atts(
		array(
			'review_url'  => '/start-review/',
			'contact_url' => '/contact/',
		),
		$atts,
		'sparq_energy_market_map'
	);

	// Only load the assets on pages that actually use the shortcode.
	wp_enqueue_style( 'sparq-emm' );
	wp_enqueue_script( 'sparq-emm' );

	ob_start();
	include SPARQ_EMM_PATH . 'templates/section.php';
	return ob_get_clean();
}
add_shortcode( 'sparq_energy_market_map', 'sparq_emm_shortcode' );
