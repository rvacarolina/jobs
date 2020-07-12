import requests
import json

cv = {
	"full_name": "Carolina Robledo Velini de Andrade",
	"email": "rvacarolina@outlook.com",
	"mobile_phone": "+55 (14) 99645-7380",
	"age": 18,
	"home_address": "Av. Professor Mello Moraes 1235, Butanta, Sao Paulo-SP, Brazil",
	"start_date": 1596366000,
	"opportunity_tag": "dev_intern_200",
	"past_jobs_experience": "I never worked formally, but, for the past 3 years I have participated in volunteer projects related to education and technology, such as Technovation Girls and Impacta Jovem Brasil. Also, I am part of the junior enterprise of my college department, IME Jr.",
	"degrees": [{
		"institution_name": "Universidade de Sao Paulo",
		"degree_name": "Bacchelor in Applied and Computational Mathematics",
		"begin_date": 1550487600,
		"end_date": 1670583600
	}],
	"programming_skills": ["python", "r", "HTML", "CSS","java"],
	"database_skills": ["postgresql"],
	"hobbies": ["yoga", "reading", "knitting"],
	"why": "Despite having experience as a volunteer in several initiatives, I feel like I need to be part of something more formal and challenging in order to improve my skills. Therefore, I want to get an internship in technology to gain experience and knowledge, besides being part of an enterprise's growth.",
	"git_url_repositories": "https://github.com/rvacarolina"
}
url = "https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume"
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(cv), headers=headers)


