import type { PageServerLoad } from './$types';
import type { ResumeData } from '$lib/types';
import { readFileSync, readdirSync } from 'fs';
import { resolve } from 'path';

export const load: PageServerLoad = async () => {
	const raw = readFileSync(resolve('resume/resume-data.json'), 'utf-8');
	const resume: ResumeData = JSON.parse(raw);

	// Find the latest versioned PDF in static/
	const staticDir = resolve('static');
	const files = readdirSync(staticDir);
	const versionedPdf = files
		.filter((f) => /^Haroun_EL_ALAMI_CV-\d{8}\.pdf$/.test(f))
		.sort()
		.pop();

	const pdfFilename = versionedPdf ?? 'Haroun_Resume.pdf';

	return { resume, pdfFilename };
};
