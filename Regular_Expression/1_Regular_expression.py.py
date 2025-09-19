#when we have to find pattern in text data so we use meta character in python
import re # first we have to import re which is inbuild module in python for regular expressing
pattern = "[A-Z]ontent"
text = ''' is a form of hypertext Pontent on the internet which is collaboratively edited and managed by its audience directly through a web browser. A typical wiki contains multiple pages that can either be edited by the public or limited to use within an organization for maintaining its internal knowledge base. Its name derives from the first user-editable website called "WikiWikiWeb", with "wiki" being a Hawaiian word meaning "quick".[1]
A photo of the MediaWiki homepage, a wiki software Wikis are powered by wiki software, also known as wiki engines. Being a form of Content management system, these differ from other web-based systems such as blog software or static site generators in that the content is created without any defined owner or leader. Wikis have little inherent'''
match=re.search(pattern,text)
print(match)