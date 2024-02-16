import re

import sys
 
fileToUpdate = sys.argv[1]

print(fileToUpdate)

nodeOpenName="22222"

nodeCloseName="44444"

def replaceCSSIncludes():

	templateSectionBegin="<styling>"

	templateSectionEnd="</styling>"

	with open('templates/html-includes-styling.template') as templateFile:

		substitutionContent = templateFile.read()

	with open(fileToUpdate) as targetSubstitutionFile:

		s = targetSubstitutionFile.read()

	ddd=s

	ddd=re.sub(templateSectionBegin, templateSectionBegin+nodeOpenName, ddd, flags=re.DOTALL)

	ddd=re.sub(templateSectionEnd, nodeCloseName+templateSectionEnd, ddd, flags=re.DOTALL)

	ddd=re.sub(nodeOpenName+".*"+nodeCloseName, substitutionContent, ddd, flags=re.DOTALL)

	f = open(fileToUpdate, "w")
	
	f.write(ddd)
	
	f.close()

def replaceJavascriptIncludes():

	templateSectionBegin="<!-- body / javascript / begin -->"

	templateSectionEnd="<!-- body / javascript / end -->"

	with open('templates/body-javascript-includes.template') as templateFile:

		substitutionContent = templateFile.read()

	with open(fileToUpdate) as targetSubstitutionFile:
		s = targetSubstitutionFile.read()

	ddd=s

	ddd=re.sub(templateSectionBegin, templateSectionBegin+nodeOpenName, ddd, flags=re.DOTALL)

	ddd=re.sub(templateSectionEnd, nodeCloseName+templateSectionEnd, ddd, flags=re.DOTALL)

	ddd=re.sub(nodeOpenName+".*"+nodeCloseName,substitutionContent,ddd,flags=re.DOTALL)

	f = open(fileToUpdate, "w")
	
	f.write(ddd)
	
	f.close()

def updateSideBarDesktop():

    templateSectionBegin="<sidebar.desktop>"

    templateSectionEnd="</sidebar.desktop>"

    with open('templates/navigation-sidebar-desktop.template') as templateFile:

        substitutionContent = templateFile.read()

    with open(fileToUpdate) as targetSubstitutionFile:

        s = targetSubstitutionFile.read()

    ddd=s

    ddd=re.sub(templateSectionBegin, templateSectionBegin+nodeOpenName, ddd, flags=re.DOTALL)

    ddd=re.sub(templateSectionEnd, nodeCloseName+templateSectionEnd, ddd, flags=re.DOTALL)

    ddd=re.sub(nodeOpenName+".*"+nodeCloseName,substitutionContent,ddd,flags=re.DOTALL)

    f = open(fileToUpdate, "w")

    f.write(ddd)

    f.close()

def updateSideBarMobile():

    templateSectionBegin="<sidebar.mobile>"

    templateSectionEnd="</sidebar.mobile>"

    with open('templates/navigation-sidebar-mobile.template') as templateFile:

        substitutionContent = templateFile.read()

    with open(fileToUpdate) as targetSubstitutionFile:

        s = targetSubstitutionFile.read()

    ddd=s

    ddd=re.sub(templateSectionBegin, templateSectionBegin+nodeOpenName, ddd, flags=re.DOTALL)

    ddd=re.sub(templateSectionEnd, nodeCloseName+templateSectionEnd, ddd, flags=re.DOTALL)

    ddd=re.sub(nodeOpenName+".*"+nodeCloseName,substitutionContent,ddd,flags=re.DOTALL)

    f = open(fileToUpdate, "w")

    f.write(ddd)

    f.close()

###################################################################
##
## driver
##
###################################################################

##replaceCSSIncludes()

replaceJavascriptIncludes()

##updateSideBarDesktop()

##updateSideBarMobile()
