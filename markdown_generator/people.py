import yaml

with open("../_data/authors.yml") as fd:
	authors = yaml.load(fd)

	for author_key in authors:

		author_info = authors[author_key]

		md_filename = author_key.replace(" ", "").lower()
		md_filepath = md_filename + ".md"

		## YAML variables
		md = ""
		md += "---\n"
		md += "layout: single\n"
		md += "collection: people\n"
		md += "title: {}\n".format(author_info["name"])
		md += "author: {}\n".format(author_key)
		md += "author_profile: true\n"
		md += "permalink: /people/{}\n".format(md_filename)
		md += "avatar: {}{}\n".format("/images/", author_info["avatar"])
		md += "tag: {}\n".format(author_info["status"])
		md += "---\n\n"
		   
		with open("../_people/" + md_filepath, 'w') as f:
		    f.write(md)
