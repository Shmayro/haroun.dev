export interface ResumeData {
	name: string;
	title: string;
	location: string;
	email: string;
	phone: string;
	linkedin: string;
	website: string;
	github: string;
	summary: string;
	summaryHighlights: string[];
	skills: Skill[];
	experience: Experience[];
	projects: Project[];
	education: Education[];
	languages: Language[];
	interests: string[];
}

export interface Skill {
	category: string;
	items: string;
}

export interface Experience {
	company: string;
	role: string | null;
	period: string;
	location: string | null;
	bullets: string[];
}

export interface Project {
	name: string;
	title: string;
	year: string;
	description: string;
	url: string | null;
	technologies?: string[];
	teamSize?: string;
	duration?: string;
}

export interface Education {
	degree: string;
	school: string;
	year: string;
}

export interface Language {
	language: string;
	level: string;
}
