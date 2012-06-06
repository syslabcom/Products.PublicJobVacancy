# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 2.0-beta1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Syslab.com GmbH <info@syslab.com>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('PublicJobVacancy: setuphandlers')
from config import DEPENDENCIES
from Products.CMFCore.utils import getToolByName
##code-section HEAD
from Products.SimpleAttachment.setuphandlers import registerImagesFormControllerActions
from Products.SimpleAttachment.setuphandlers import registerAttachmentsFormControllerActions
##/code-section HEAD


def installGSDependencies(context):
    """Install dependend profiles."""

    # XXX Hacky, but works for now. has to be refactored as soon as generic
    # setup allows a more flexible way to handle dependencies.

    dependencies = []
    if not dependencies:
        return

    site = context.getSite()
    setup_tool = getToolByName(site, 'portal_setup')
    for dependency in dependencies:
        if dependency.find(':') == -1:
            dependency += ':default'
        old_context = setup_tool.getImportContextID()
        setup_tool.setImportContext('profile-%s' % dependency)
        importsteps = setup_tool.getImportStepRegistry().sortSteps()
        excludes = [
            u'PublicJobVacancy-QI-dependencies',
            u'PublicJobVacancy-GS-dependencies'
        ]
        importsteps = [s for s in importsteps if s not in excludes]
        for step in importsteps:
            setup_tool.runImportStep(step)  # purging flag here?
        setup_tool.setImportContext(old_context)

    # re-run some steps to be sure the current profile applies as expected
    importsteps = setup_tool.getImportStepRegistry().sortSteps()
    filter = [
        u'typeinfo',
        u'workflow',
        u'membranetool',
        u'factorytool',
        u'content_type_registry',
        u'membrane-sitemanager'
    ]
    importsteps = [s for s in importsteps if s in filter]
    for step in importsteps:
        setup_tool.runImportStep(step)  # purging flag here?


def installQIDependencies(context):
    """This is for old-style products using QuickInstaller"""
    site = context.getSite()
    qi = getToolByName(site, 'portal_quickinstaller')
    for dependency in DEPENDENCIES:
        if qi.isProductInstalled(dependency):
            logger.info("Re-Installing dependency %s:" % dependency)
            qi.reinstallProducts([dependency])
        else:
            logger.info("Installing dependency %s:" % dependency)
            qi.installProducts([dependency])


##code-section FOOT
def installAttachmentSupport(context):
    """ install attachment handlers """
    site = context.getSite()
    # Set up form controller actions for the widgets to work
    registerAttachmentsFormControllerActions(
        site, contentType='PublicJobVacancy', template='base_edit')
    registerImagesFormControllerActions(
        site, contentType='PublicJobVacancy', template='base_edit')

    # Register form controller actions for LinguaPlone translate_item
    registerAttachmentsFormControllerActions(
        site, contentType='PublicJobVacancy', template='translate_item')
    registerImagesFormControllerActions(
        site, contentType='PublicJobVacancy', template='translate_item')
##/code-section FOOT
