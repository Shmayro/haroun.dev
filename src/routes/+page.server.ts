import type { PageServerLoad } from './$types';
import type { ResumeData } from '$lib/types';
import { readFileSync } from 'fs';
import { resolve } from 'path';

export const load: PageServerLoad = async () => {
	const raw = readFileSync(resolve('resume/resume-data.json'), 'utf-8');
	const resume: ResumeData = JSON.parse(raw);
	return { resume };
};
