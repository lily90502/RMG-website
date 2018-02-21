#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#                                                                             #
# RMG Website - A Django-powered website for Reaction Mechanism Generator     #
#                                                                             #
# Copyright (c) 2011-2018 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

import itertools
from django.conf.urls import url, include
from rmgweb.database import views


urlpatterns = [ 

    # Database homepage
    url(r'^$', views.index),
    
    # Load the whole database into memory
    url(r'^load/?$', views.load),
    
    # Export to an RMG-Java database
    url(r'^export_(?P<type>zip|tar\.gz)/?$', views.export),

    # Thermodynamics database
    url(r'^thermo/$', views.thermo),
    url(r'^thermo/search/$', views.moleculeSearch),
    url(r'^thermo/molecule/(?P<adjlist>[\S\s]+)$', views.thermoData),
    url(r'^thermo/(?P<section>\w+)/(?P<subsection>.+)/(?P<index>-?\d+)/$', views.thermoEntry),
    url(r'^thermo/(?P<section>\w+)/(?P<subsection>.+)/(?P<adjlist>[\S\s]+)/new$', views.thermoEntryNew),
    url(r'^thermo/(?P<section>\w+)/(?P<subsection>.+)/(?P<index>-?\d+)/edit$', views.thermoEntryEdit),
    url(r'^thermo/(?P<section>\w+)/(?P<subsection>.+)/$', views.thermo),
    url(r'^thermo/(?P<section>\w+)/$', views.thermo),
    
    # Transport database
    url(r'^transport/$', views.transport),
    url(r'^transport/search/$', views.moleculeSearch),
    url(r'^transport/molecule/(?P<adjlist>[\S\s]+)$', views.transportData),
    url(r'^transport/(?P<section>\w+)/(?P<subsection>.+)/(?P<index>-?\d+)/$', views.transportEntry),
    url(r'^transport/(?P<section>\w+)/(?P<subsection>.+)/$', views.transport),
    url(r'^transport/(?P<section>\w+)/$', views.transport),    
    
    # solvation database
    url(r'^solvation/$', views.solvation),
    url(r'^solvation/search/$', views.solvationSearch),    
    url(r'^solvation/results/solute=(?P<solute_adjlist>[\S\s]+)__solvent=(?P<solvent>[\S\s]+)$', views.solvationData),    
    url(r'^solvation/(?P<section>\w+)/(?P<subsection>.+)/(?P<index>-?\d+)/$', views.solvationEntry),
    url(r'^solvation/(?P<section>\w+)/(?P<subsection>.+)/$', views.solvation),
    url(r'^solvation/(?P<section>\w+)/$', views.solvation),   
    
    # statmech database
    url(r'^statmech/$', views.statmech),
    url(r'^statmech/search/$', views.moleculeSearch),
    url(r'^statmech/molecule/(?P<adjlist>[\S\s]+)$', views.statmechData),
    url(r'^statmech/(?P<section>\w+)/(?P<subsection>.+)/(?P<index>-?\d+)/$', views.statmechEntry),
    url(r'^statmech/(?P<section>\w+)/(?P<subsection>.+)/$', views.statmech),
    url(r'^statmech/(?P<section>\w+)/$', views.statmech), 
    
    # Kinetics database
    url(r'^kinetics/$', views.kinetics),
    url(r'^kinetics/search/$', views.kineticsSearch),

    url(r'^kinetics/families/(?P<family>[^/]+)/(?P<type>\w+)/new$', views.kineticsEntryNew),
    url(r'^kinetics/families/(?P<family>[^/]+)/untrained/$', views.kineticsUntrained),
    
    url(r'^kinetics/(?P<section>\w+)/(?P<subsection>.+)/(?P<index>\d+)/edit$', views.kineticsEntryEdit),
    url(r'^kinetics/(?P<section>\w+)/(?P<subsection>.+)/(?P<index>-?\d+)/$', views.kineticsEntry),
    url(r'^kinetics/(?P<section>\w+)/(?P<subsection>.+)/$', views.kinetics),
    url(r'^kinetics/(?P<section>\w+)/$', views.kinetics),
    
    # Molecule Information Page
    url(r'^molecule/(?P<adjlist>[\S\s]+)$', views.moleculeEntry),
    
    #Group Information Page
    url(r'^group/(?P<adjlist>[\S\s]+)$', views.groupEntry),

    # Eni detergent-dirt binding strength
    url(r'^eni', views.EniSearch),

    # AJAX request url
    url(r'^ajax_adjlist_request', views.json_to_adjlist),

    # Remember to update the /media/robots.txt file to keep web-crawlers out of pages you don't want indexed.
]

# Generate url patterns for kinetics search and results pages combinatorially
url_parts = [
    r'reactant1=(?P<reactant1>[\S\s]+)',
    r'__reactant2=(?P<reactant2>[\S\s]+)',
    r'__reactant3=(?P<reactant3>[\S\s]+)',
    r'__product1=(?P<product1>[\S\s]+)',
    r'__product2=(?P<product2>[\S\s]+)',
    r'__product3=(?P<product3>[\S\s]+)',
    r'__res=(?P<resonance>[\S\s]+)',
]

for r2, r3, p1, p2, p3, res in itertools.product([1, 0], repeat=6):
    url_pattern = r'^kinetics/results/'
    url_pattern += url_parts[0]
    if r2: url_pattern += url_parts[1]
    if r2 and r3: url_pattern += url_parts[2]
    if p1: url_pattern += url_parts[3]
    if p2: url_pattern += url_parts[4]
    if p2 and p3: url_pattern += url_parts[5]
    if res: url_pattern += url_parts[6]
    url_pattern += r'$'

    urlpatterns.append(url(url_pattern, views.kineticsResults))

for r2, r3, p1, p2, p3, res in itertools.product([1, 0], repeat=6):
    url_pattern = r'^kinetics/reaction/'
    url_pattern += url_parts[0]
    if r2: url_pattern += url_parts[1]
    if r2 and r3: url_pattern += url_parts[2]
    if p1: url_pattern += url_parts[3]
    if p2: url_pattern += url_parts[4]
    if p2 and p3: url_pattern += url_parts[5]
    if res: url_pattern += url_parts[6]
    url_pattern += r'$'

    urlpatterns.append(url(url_pattern, views.kineticsData))

for r2, p2, res in itertools.product([1, 0], repeat=3):
    url_pattern = r'^kinetics/families/(?P<family>[^/]+)/(?P<estimator>[^/]+)/'
    url_pattern += url_parts[0]
    if r2: url_pattern += url_parts[1]
    url_pattern += url_parts[3]
    if p2: url_pattern += url_parts[4]
    if res: url_pattern += url_parts[6]
    url_pattern += r'$'

    urlpatterns.append(url(url_pattern, views.kineticsGroupEstimateEntry))
