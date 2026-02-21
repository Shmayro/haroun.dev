<script lang="ts">
	import type { ResumeData } from '$lib/types';

	let { data } = $props();
	let resume: ResumeData = $derived(data.resume);
	let pdfFilename: string = $derived(data.pdfFilename);

	let highlightedSummary: string = $derived.by(() => {
		let html = resume.summary;
		for (const phrase of resume.summaryHighlights ?? []) {
			html = html.replace(phrase, `<strong>${phrase}</strong>`);
		}
		return html;
	});
</script>

<svelte:head>
	<title>{resume.name} — {resume.title}</title>
	<meta name="description" content={resume.summary} />
</svelte:head>

<div class="resume">
	<!-- Header -->
	<header class="header">
		<div class="header-identity">
			<h1 class="name">{resume.name}</h1>
			<p class="title">{resume.title}</p>
		</div>
		<div class="header-contact">
			<ul class="contact-list">
				<li>
					<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
					{resume.location}
				</li>
				<li>
					<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
					<a href="mailto:{resume.email}">{resume.email}</a>
				</li>
				<li>
					<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
					<a href="tel:{resume.phone}">{resume.phone}</a>
				</li>
			</ul>
			<ul class="links-list">
				<li>
					<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
					<a href="https://{resume.linkedin}" target="_blank" rel="noopener noreferrer">{resume.linkedin}</a>
				</li>
				<li>
					<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>
					<a href="https://{resume.website}" target="_blank" rel="noopener noreferrer">{resume.website}</a>
				</li>
				<li>
					<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/></svg>
					<a href="https://{resume.github}" target="_blank" rel="noopener noreferrer">{resume.github}</a>
				</li>
			</ul>
		</div>
		<div class="header-cta">
			<a href="/{pdfFilename}" class="download-btn" download={pdfFilename}>
				<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
				Download PDF
			</a>
		</div>
	</header>

	<!-- Professional Summary -->
	<section class="section" aria-labelledby="summary-heading">
		<h2 id="summary-heading" class="section-heading">Professional Summary</h2>
		<p class="summary-text">{@html highlightedSummary}</p>
	</section>

	<!-- Core Skills -->
	<section class="section" aria-labelledby="skills-heading">
		<h2 id="skills-heading" class="section-heading">Core Skills</h2>
		<dl class="skills-grid">
			{#each resume.skills as skill (skill.category)}
				<div class="skill-row">
					<dt class="skill-category">{skill.category}</dt>
					<dd class="skill-items">{skill.items}</dd>
				</div>
			{/each}
		</dl>
	</section>

	<!-- Professional Experience -->
	<section class="section" aria-labelledby="experience-heading">
		<h2 id="experience-heading" class="section-heading">Professional Experience</h2>
		<div class="experience-list">
			{#each resume.experience as job (job.company)}
				<article class="experience-item">
					<div class="experience-header">
						<div class="experience-title-group">
							<h3 class="experience-company">{job.company}</h3>
							{#if job.role}
								<p class="experience-role">{job.role}</p>
							{/if}
						</div>
						<div class="experience-meta">
							<span class="chip">{job.period}</span>
							{#if job.location}
								<span class="location-label">{job.location}</span>
							{/if}
						</div>
					</div>
					<ul class="experience-bullets">
						{#each job.bullets as bullet, i (i)}
							<li>{bullet}</li>
						{/each}
					</ul>
				</article>
			{/each}
		</div>
	</section>

	<!-- Personal Projects -->
	<section class="section" aria-labelledby="projects-heading">
		<h2 id="projects-heading" class="section-heading">Personal Projects</h2>
		<div class="projects-grid">
			{#each resume.projects as project (project.name)}
				<article class="project-card">
					<div class="project-header">
						<h3 class="project-name">{project.name}</h3>
						<span class="chip chip-small">{project.year}</span>
					</div>
					<p class="project-title">{project.title}</p>
					<p class="project-description">{project.description}</p>
					{#if project.url}
						<a href={project.url} class="project-link" target="_blank" rel="noopener noreferrer">
							<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
							View on GitHub
						</a>
					{/if}
				</article>
			{/each}
		</div>
	</section>

	<!-- Education -->
	<section class="section" aria-labelledby="education-heading">
		<h2 id="education-heading" class="section-heading">Education</h2>
		<div class="education-list">
			{#each resume.education as edu (edu.degree)}
				<div class="education-item">
					<div class="education-info">
						<h3 class="education-degree">{edu.degree}</h3>
						<p class="education-school">{edu.school}</p>
					</div>
					<span class="chip chip-small">{edu.year}</span>
				</div>
			{/each}
		</div>
	</section>

	<!-- Languages -->
	<section class="section" aria-labelledby="languages-heading">
		<h2 id="languages-heading" class="section-heading">Languages</h2>
		<ul class="inline-list">
			{#each resume.languages as lang (lang.language)}
				<li class="inline-item">
					<strong>{lang.language}</strong>
					<span class="level-badge">{lang.level}</span>
				</li>
			{/each}
		</ul>
	</section>

	<!-- Interests -->
	<section class="section" aria-labelledby="interests-heading">
		<h2 id="interests-heading" class="section-heading">Interests</h2>
		<ul class="tag-cloud">
			{#each resume.interests as interest (interest)}
				<li class="tag">{interest}</li>
			{/each}
		</ul>
	</section>

	<!-- Footer -->
	<footer class="footer">
		<p>Last updated February 2026</p>
	</footer>
</div>

<style>
	/* ========================================
	   Design Tokens
	   ======================================== */
	:root {
		--color-accent: #2874A6;
		--color-accent-light: #eef6fc;
		--color-accent-hover: #1f5f8b;
		--color-heading: #2E4053;
		--color-subtitle: #34495E;
		--color-text: #1f2937;
		--color-muted: #6b7280;
		--color-bg: #ffffff;
		--color-rule: #e5e7eb;
		--color-chip-bg: #eef6fc;
		--color-chip-text: #2874A6;
		--font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
		--max-width: 860px;
		--radius: 6px;
		--radius-lg: 10px;
	}

	/* ========================================
	   Layout
	   ======================================== */
	.resume {
		max-width: var(--max-width);
		margin: 0 auto;
		padding: 48px 32px 32px;
		font-family: var(--font-body);
		font-size: 15px;
		line-height: 1.55;
		color: var(--color-text);
		background: var(--color-bg);
	}

	/* ========================================
	   Header
	   ======================================== */
	.header {
		display: grid;
		grid-template-columns: 1fr auto;
		grid-template-rows: auto auto;
		gap: 16px 32px;
		padding-bottom: 32px;
		border-bottom: 2px solid var(--color-accent);
		margin-bottom: 36px;
	}

	.header-identity {
		grid-column: 1 / -1;
	}

	.name {
		font-size: 2.2rem;
		font-weight: 800;
		color: var(--color-heading);
		margin: 0;
		letter-spacing: -0.5px;
		line-height: 1.15;
	}

	.title {
		font-size: 1.1rem;
		color: var(--color-accent);
		margin: 6px 0 0;
		font-weight: 500;
	}

	.header-contact {
		grid-column: 1;
	}

	.contact-list,
	.links-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-wrap: wrap;
		gap: 6px 20px;
		font-size: 0.9rem;
	}

	.links-list {
		margin-top: 6px;
	}

	.contact-list li,
	.links-list li {
		display: flex;
		align-items: center;
		gap: 5px;
		color: var(--color-muted);
	}

	.contact-list a,
	.links-list a {
		color: var(--color-accent);
		text-decoration: none;
		border-bottom: 1px solid transparent;
		transition: border-color 0.2s;
	}

	.contact-list a:hover,
	.links-list a:hover {
		border-bottom-color: var(--color-accent);
	}

	.icon {
		width: 15px;
		height: 15px;
		flex-shrink: 0;
	}

	.header-cta {
		grid-column: 2;
		grid-row: 2;
		align-self: start;
	}

	.download-btn {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		padding: 10px 22px;
		background: var(--color-accent);
		color: #fff;
		text-decoration: none;
		border-radius: var(--radius-lg);
		font-size: 0.9rem;
		font-weight: 600;
		transition: background-color 0.2s, transform 0.1s;
		white-space: nowrap;
	}

	.download-btn:hover {
		background: var(--color-accent-hover);
		transform: translateY(-1px);
	}

	.download-btn:active {
		transform: translateY(0);
	}

	.download-btn .icon {
		width: 16px;
		height: 16px;
		stroke: #fff;
	}

	/* ========================================
	   Section Headings
	   ======================================== */
	.section {
		margin-bottom: 32px;
	}

	.section-heading {
		font-size: 1.15rem;
		font-weight: 700;
		color: var(--color-heading);
		text-transform: uppercase;
		letter-spacing: 1.5px;
		margin: 0 0 16px;
		padding-bottom: 8px;
		border-bottom: 1px solid var(--color-rule);
		position: relative;
	}

	.section-heading::after {
		content: '';
		position: absolute;
		bottom: -1px;
		left: 0;
		width: 48px;
		height: 2px;
		background: var(--color-accent);
	}

	/* ========================================
	   Professional Summary
	   ======================================== */
	.summary-text {
		margin: 0;
		color: var(--color-subtitle);
		line-height: 1.7;
	}

	/* ========================================
	   Skills
	   ======================================== */
	.skills-grid {
		margin: 0;
		display: grid;
		gap: 0;
	}

	.skill-row {
		display: grid;
		grid-template-columns: 180px 1fr;
		gap: 12px;
		padding: 10px 0;
		border-bottom: 1px solid var(--color-rule);
		align-items: baseline;
	}

	.skill-row:last-child {
		border-bottom: none;
	}

	.skill-category {
		font-weight: 700;
		font-size: 0.88rem;
		color: var(--color-heading);
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}

	.skill-items {
		margin: 0;
		color: var(--color-text);
	}

	/* ========================================
	   Experience
	   ======================================== */
	.experience-list {
		display: flex;
		flex-direction: column;
		gap: 28px;
	}

	.experience-item {
		position: relative;
		padding-left: 20px;
	}

	.experience-item::before {
		content: '';
		position: absolute;
		left: 0;
		top: 6px;
		bottom: 0;
		width: 3px;
		background: linear-gradient(to bottom, var(--color-accent), var(--color-accent-light));
		border-radius: 2px;
	}

	.experience-header {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
		gap: 12px;
		flex-wrap: wrap;
		margin-bottom: 10px;
	}

	.experience-title-group {
		min-width: 0;
	}

	.experience-company {
		font-size: 1.05rem;
		font-weight: 700;
		color: var(--color-heading);
		margin: 0;
	}

	.experience-role {
		font-size: 0.95rem;
		color: var(--color-subtitle);
		margin: 2px 0 0;
		font-style: italic;
	}

	.experience-meta {
		display: flex;
		flex-direction: column;
		align-items: flex-end;
		gap: 4px;
		flex-shrink: 0;
	}

	.chip {
		display: inline-block;
		padding: 4px 14px;
		background: var(--color-chip-bg);
		color: var(--color-chip-text);
		font-size: 0.82rem;
		font-weight: 600;
		border-radius: 100px;
		white-space: nowrap;
	}

	.chip-small {
		padding: 3px 10px;
		font-size: 0.78rem;
	}

	.location-label {
		font-size: 0.82rem;
		color: var(--color-muted);
	}

	.experience-bullets {
		margin: 0;
		padding-left: 18px;
		list-style-type: disc;
	}

	.experience-bullets li {
		margin-bottom: 4px;
		line-height: 1.55;
	}

	.experience-bullets li::marker {
		color: var(--color-accent);
	}

	/* ========================================
	   Projects
	   ======================================== */
	.projects-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
		gap: 16px;
	}

	.project-card {
		padding: 18px 20px;
		border: 1px solid var(--color-rule);
		border-radius: var(--radius-lg);
		transition: border-color 0.2s, box-shadow 0.2s;
	}

	.project-card:hover {
		border-color: var(--color-accent);
		box-shadow: 0 2px 12px rgba(40, 116, 166, 0.08);
	}

	.project-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 8px;
		margin-bottom: 4px;
	}

	.project-name {
		font-size: 1rem;
		font-weight: 700;
		color: var(--color-heading);
		margin: 0;
		font-family: 'SF Mono', 'Fira Code', 'Fira Mono', Menlo, Consolas, monospace;
	}

	.project-title {
		font-size: 0.88rem;
		color: var(--color-muted);
		margin: 0 0 8px;
	}

	.project-description {
		font-size: 0.92rem;
		margin: 0;
		line-height: 1.55;
	}

	.project-link {
		display: inline-flex;
		align-items: center;
		gap: 5px;
		margin-top: 10px;
		font-size: 0.85rem;
		font-weight: 600;
		color: var(--color-accent);
		text-decoration: none;
		transition: color 0.2s;
	}

	.project-link:hover {
		color: var(--color-accent-hover);
	}

	.project-link .icon {
		width: 13px;
		height: 13px;
	}

	/* ========================================
	   Education
	   ======================================== */
	.education-list {
		display: flex;
		flex-direction: column;
		gap: 14px;
	}

	.education-item {
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 12px;
		padding: 10px 0;
		border-bottom: 1px solid var(--color-rule);
	}

	.education-item:last-child {
		border-bottom: none;
	}

	.education-info {
		min-width: 0;
	}

	.education-degree {
		font-size: 0.95rem;
		font-weight: 600;
		color: var(--color-heading);
		margin: 0;
	}

	.education-school {
		font-size: 0.88rem;
		color: var(--color-muted);
		margin: 2px 0 0;
	}

	/* ========================================
	   Languages
	   ======================================== */
	.inline-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-wrap: wrap;
		gap: 12px;
	}

	.inline-item {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 8px 16px;
		background: var(--color-chip-bg);
		border-radius: var(--radius);
		font-size: 0.92rem;
	}

	.inline-item strong {
		color: var(--color-heading);
	}

	.level-badge {
		font-size: 0.8rem;
		color: var(--color-muted);
		font-style: italic;
	}

	/* ========================================
	   Interests
	   ======================================== */
	.tag-cloud {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.tag {
		padding: 6px 16px;
		border: 1px solid var(--color-rule);
		border-radius: 100px;
		font-size: 0.88rem;
		color: var(--color-subtitle);
		transition: border-color 0.2s, color 0.2s;
	}

	.tag:hover {
		border-color: var(--color-accent);
		color: var(--color-accent);
	}

	/* ========================================
	   Footer
	   ======================================== */
	.footer {
		margin-top: 40px;
		padding-top: 20px;
		border-top: 1px solid var(--color-rule);
		text-align: center;
		font-size: 0.82rem;
		color: var(--color-muted);
	}

	.footer p {
		margin: 0;
	}

	/* ========================================
	   Responsive
	   ======================================== */
	@media (max-width: 680px) {
		.resume {
			padding: 24px 16px 24px;
		}

		.header {
			grid-template-columns: 1fr;
			gap: 16px;
		}

		.header-cta {
			grid-column: 1;
			grid-row: auto;
		}

		.download-btn {
			width: 100%;
			justify-content: center;
		}

		.name {
			font-size: 1.65rem;
		}

		.skill-row {
			grid-template-columns: 1fr;
			gap: 2px;
		}

		.experience-header {
			flex-direction: column;
		}

		.experience-meta {
			align-items: flex-start;
			flex-direction: row;
			gap: 8px;
		}

		.projects-grid {
			grid-template-columns: 1fr;
		}

		.education-item {
			flex-direction: column;
			align-items: flex-start;
			gap: 6px;
		}
	}

	/* ========================================
	   Print
	   ======================================== */
	@media print {
		.resume {
			padding: 0;
			font-size: 12px;
			max-width: none;
		}

		.header {
			border-bottom-width: 1px;
		}

		.header-cta {
			display: none;
		}

		.section-heading::after {
			display: none;
		}

		.project-card {
			border: 1px solid var(--color-rule);
			box-shadow: none;
			break-inside: avoid;
		}

		.project-card:hover {
			border-color: var(--color-rule);
			box-shadow: none;
		}

		.experience-item {
			break-inside: avoid;
		}

		.tag:hover {
			border-color: var(--color-rule);
			color: var(--color-subtitle);
		}

		a {
			text-decoration: none;
		}
	}
</style>
