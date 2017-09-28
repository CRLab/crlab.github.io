import yaml

with open("../_data/authors.yml") as fd:
	authors = yaml.load(fd)

	for author in authors:

		md_filename = str(item["pub_date"]) + "-" + item["url_slug"] + ".md"
		html_filename = str(item["pub_date"]) + "-" + item["url_slug"]
		year = item["pub_date"][:4]

		## YAML variables

		md = "---\ntitle: \""   + item["title"] + '"\n'

		md += """collection: publications"""

		md += """\npermalink: /publication/""" + html_filename

		if len(str(item["excerpt"])) > 5:
		    md += "\nexcerpt: '" + html_escape(item["excerpt"]) + "'"

		md += "\ndate: " + str(item["pub_date"]) 

		md += "\nvenue: '" + html_escape(item["venue"]) + "'"

		if len(str(item["paper_url"])) > 5:
		    md += "\npaperurl: '" + item["paper_url"] + "'"

		md += "\ncitation: '" + html_escape(item["citation"]) + "'"

		md += "\nauthor: '" + html_escape(item["first-author"]) + "'"

		md += "\nauthor_profile: true"

		md += "\nauthors: '" + html_escape(item["authors"]) + "'"

		md += "\nlocation: '" + html_escape(item["location"]) + "'"

		md += "\nkeywords: '" + html_escape(item["keywords"]) + "'"

		md += "\n---"

		## Markdown description for individual page
		    
		if len(str(item["abstract"])) > 5:
		    md += "\n" + html_escape(item["abstract"]) + "\n"
		    
		md += "\nRecommended citation: " + item["citation"]

		if len(str(item["paper_url"])) > 5:
		    md += "\n\n<a href='" + item["paper_url"] + "'>Download paper here</a>\n" 

		md_filename = os.path.basename(md_filename)
		   
		with open("../_publications/" + md_filename, 'w') as f:
		    f.write(md)