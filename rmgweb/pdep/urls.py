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

from django.conf.urls import url, include
from rmgweb.pdep import views
urlpatterns = [
    # Pressure dependence homepage
    url(r'^$', views.index),

    # URL for beginning a new calculation
    url(r'^start$', views.start),

    # URL for the main page of an individual Network
    url(r'^networks/(?P<networkKey>[^/]+)$', views.networkIndex),
    
    # URLs for various methods of adding/editing input parameters
    url(r'^networks/(?P<networkKey>[^/]+)/edit$', views.networkEditor),
    url(r'^networks/(?P<networkKey>[^/]+)/upload$', views.networkUpload),

    # URLs for generating various output files
    url(r'^networks/(?P<networkKey>[^/]+)/draw/png$', views.networkDrawPNG),
    url(r'^networks/(?P<networkKey>[^/]+)/draw/pdf$', views.networkDrawPDF),
    url(r'^networks/(?P<networkKey>[^/]+)/draw/svg$', views.networkDrawSVG),
    url(r'^networks/(?P<networkKey>[^/]+)/run$', views.networkRun),
    
    # URLs for browsing network information
    url(r'^networks/(?P<networkKey>[^/]+)/species/(?P<species>[^/]+)$', views.networkSpecies),
    url(r'^networks/(?P<networkKey>[^/]+)/pathReactions/(?P<reaction>[^/]+)$', views.networkPathReaction),
    url(r'^networks/(?P<networkKey>[^/]+)/netReactions/(?P<reaction>[^/]+)$', views.networkNetReaction),
    url(r'^networks/(?P<networkKey>[^/]+)/kinetics$', views.networkPlotKinetics),
    url(r'^networks/(?P<networkKey>[^/]+)/microdata$', views.networkPlotMicro),
    
    # Delete a network    
    url(r'^networks/(?P<networkKey>[^/]+)/delete$', views.networkDelete),
    
]
