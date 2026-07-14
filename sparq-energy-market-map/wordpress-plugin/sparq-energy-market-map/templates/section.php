<?php
/**
 * Front-end markup for the SPARQ Energy Market Map.
 *
 * Rendered by the [sparq_energy_market_map] shortcode.
 * $atts is provided by the shortcode callback (review_url, contact_url).
 *
 * @var array $atts
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$review_url  = isset( $atts['review_url'] ) ? $atts['review_url'] : '/start-review/';
$contact_url = isset( $atts['contact_url'] ) ? $atts['contact_url'] : '/contact/';
?>
<section id="sparq-energy-market-map" class="sparq-energy-section">
	<div class="sparq-energy-inner">
		<div class="sparq-eyebrow">Energy Market Eligibility</div>

		<h2>Energy Opportunities Vary by Market</h2>

		<p class="sparq-lead">
			In deregulated or retail choice markets, businesses may have the ability to review competitive supply options while the local utility continues to deliver service. Availability can vary by state, utility territory, account type, and market rules, which is why SPARQ reviews each energy account individually.
		</p>

		<div class="sparq-map-card">
			<div class="sparq-map-panel">
				<div class="sparq-map-controls" aria-label="Energy market map controls">
					<button class="sparq-toggle active" type="button" data-market="electricity">Electricity</button>
					<button class="sparq-toggle" type="button" data-market="gas">Natural Gas</button>
				</div>

				<div id="sparq-us-energy-map"></div>

				<p class="sparq-map-note">
					This map is for general education only. Energy choice, supplier availability, and potential savings may vary by utility territory, customer type, and current market conditions.
				</p>
			</div>

			<aside class="sparq-side-panel">
				<div>
					<h3 id="sparq-market-title">Electricity Retail Choice</h3>
					<p id="sparq-market-description" class="sparq-market-description">
						Some states allow electricity customers to choose a competitive supplier, while the local utility continues to deliver power and maintain the infrastructure.
					</p>

					<div class="sparq-legend">
						<div class="sparq-legend-item">
							<span class="sparq-dot sparq-dot-full"></span>
							<span id="sparq-full-label">Deregulated / retail choice</span>
						</div>
						<div class="sparq-legend-item">
							<span class="sparq-dot sparq-dot-limited"></span>
							<span id="sparq-limited-label">Limited or utility-specific choice</span>
						</div>
						<div class="sparq-legend-item">
							<span class="sparq-dot sparq-dot-regulated"></span>
							<span>Regulated / no broad retail choice</span>
						</div>
					</div>

					<div id="sparq-state-list" class="sparq-state-list"></div>
				</div>

				<div class="sparq-energy-cta">
					<a class="sparq-btn-primary" href="<?php echo esc_url( $review_url ); ?>">Start Review</a>
					<a class="sparq-btn-secondary" href="<?php echo esc_url( $contact_url ); ?>">Contact Us</a>
				</div>
			</aside>
		</div>
	</div>
</section>
