from string import Template

#defines different top, content, and bottom of html files
top = open('./templates/top.html').read()
index = open('./content/index.html').read()
projects = open('./content/toolset.html').read()
contact = open('./content/contact.html').read()
bottom = open('./templates/bottom.html').read()

#defines how full html files are concatenated
full_index = top + index + bottom
full_projects = top + projects + bottom
full_contact = top + contact + bottom


#writes full pages to single file and substitutes active classes of navbars
open('./docs/index.html', "w").write(full_index)

active_class = open('./docs/index.html').read()
template = Template(active_class)
open('./docs/index.html', 'w').write((template.safe_substitute(active_home='class= "nav-item home-active"')))
open('./docs/index.html', 'w').write((template.safe_substitute(active_projects='class= "nav-item')))
open('./docs/index.html', 'w').write((template.safe_substitute(active_contact='class= "nav-item')))


open('./docs/projects.html', "w").write(full_projects)

active_class = open('./docs/projects.html').read()
template = Template(active_class)
open('./docs/projects.html', 'w').write((template.safe_substitute(active_home='class= "nav-item"')))
open('./docs/projects.html', 'w').write((template.safe_substitute(active_projects='class= "nav-item home-active')))
open('./docs/projects.html', 'w').write((template.safe_substitute(active_contact='class= "nav-item')))


open('./docs/contact.html', "w").write(full_contact)

active_class = open('./docs/contact.html').read()
template = Template(active_class)
open('./docs/contact.html', 'w').write((template.safe_substitute(active_home='class= "nav-item"')))
open('./docs/contact.html', 'w').write((template.safe_substitute(active_projects='class= "nav-item')))
open('./docs/contact.html', 'w').write((template.safe_substitute(active_contact='class= "nav-item home-active')))


print("done.") 