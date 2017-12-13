# DICE-Profiles
UML profiles for the DICE project

# Installing the Profiles

In Eclipse, go to `Help -> Install New Software...` and use http://dice-project.github.io/DICE-Profiles/updates as the URL for the update site.

# Contents

## Examples - [org.dice.profiles.examples](https://github.com/dice-project/DICE-Profiles/tree/master/org.dice.profiles.examples)

This project contains some Papyrus UML models demonstrating some DICE Profile annotations.

## es.unizar.disco.dice.static.profile

This plugin implement the DICE profile using the same system as MARTE to define NFP datatypes. To generate the DICE.ecore model from the DICE.profile.uml the patched `org.eclipse.uml2.uml` plugin is needed.

## es.unizar.disco.dice.feature

Feature for the DICE Profile.

## com.masdes.dam.static.profile

This plugin reimplements the DAM profile available at https://bitbucket.org/mberenguer/masdes-downloads/wiki/Home, and unifies the type system, solving problems with the redefinition of MARTE datatypes.
To generate the DAM.ecore model from the DAM.profile.uml the patched `org.eclipse.uml2.uml` plugin is needed.

## com.masdes.dam.profile.feature

Feature for the DAM Profile.

## com.masdes.dam.static.profile.ui

UI enhancements for the DAM profile, such as icons and custom label providers for the 'Properties' view.

## com.masdes.dam.profile.ui.feature

Feature for the UI enhancements of the DAM Profile.

## org.eclipse.uml2.uml

This plugin is a patched version of `org.eclipse.uml2.uml` that eases the generation of profiles based on Papyrus MARTE.
It is only required for generating the Ecore file that implements a UML profile.
