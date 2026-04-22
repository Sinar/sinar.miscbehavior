.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://img.shields.io/pypi/v/sinar.miscbehavior.svg
    :target: https://pypi.python.org/pypi/sinar.miscbehavior/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/sinar.miscbehavior.svg?style=plastic
    :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/sinar.miscbehavior.svg
    :target: https://pypi.python.org/pypi/sinar.miscbehavior/
    :alt: License


======================
sinar.miscbehavior
======================

Misc behaviors for Sinar civil society site content types.

This add-on provides reusable Dexterity behaviors and vocabularies for
categorizing and assessing content related to civil society, development
work, and digital rights.

Features
--------

**Dexterity Behaviors:**

- **Assessment** — Rich text field for MEL assessment notes, with guided
  prompts for partnerships, beneficiary involvement, gender/ethnic issues,
  and implementation reflections.
- **Countries** — Multi-select list of ISO countries for geographic
  categorization.
- **Development Themes** — Multi-select from 27 development themes including
  Accessibility, Agriculture, Education, Health, Human Rights, Peacebuilding,
  Women and Gender, Youth Development, and more.
- **Digital Rights** — Multi-select from 17 digital rights and tech
  accountability categories including AI, Algorithmic Accountability,
  Cybersecurity, Privacy and Surveillance, Open Data, and Internet
  Governance.
- **Dissemination** — Adds a project name text field and a boolean
  dissemination marker to label content as project dissemination material.
- **SDG Goals** — Multi-select from all 169 UN Sustainable Development Goal
  targets across the 17 goals.
- **Website URL** — URI field for linking to external websites or content.

**Vocabularies:**

- **Development Themes** — 27 themes covering areas from agriculture and
  health to legislative assemblies and procurement.
- **Digital Rights** — 17 categories covering AI, cloud computing, consumer
  safety, cybercrime, intellectual property, platform accountability, and
  more.
- **SDG Goals** — All 169 SDG targets with full descriptive text.
- **Marginalized Communities Malaysia** — 9 categories including Orang Asal
  (Sabah/Sarawak), refugees, stateless persons, persons with disabilities,
  and others.

**Catalog Indexes:**

- ``development_themes`` — KeywordIndex
- ``SDG_goals`` — KeywordIndex
- ``digital_rights_categories`` — KeywordIndex
- ``countries`` — KeywordIndex

**Query String Fields:**

- ``countries`` — Filter by ISO country
- ``SDG_goals`` — Filter by SDG target
- ``digital_rights_categories`` — Filter by digital rights category

Installation
------------

Install sinar.miscbehavior by adding it to your buildout::

    [buildout]

    ...

    eggs =
        sinar.miscbehavior


and then running ``bin/buildout``

Contribute
----------

- Issue Tracker: https://github.com/Sinar/sinar.miscbehavior/issues
- Source Code: https://github.com/Sinar/sinar.miscbehavior

Support
-------

If you are having issues, please let us know.

License
-------

The project is licensed under the GPLv2.
