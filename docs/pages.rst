.. _pages:

Controlling Site Content
========================

The BAP Website uses a `Content Management System (CMS) <http://en.wikipedia.org/wiki/Content_management_system>`_ to allow users to edit content on specific pages with their browser. It's also possible to lay out pages in a hierarchy and to make links between pages in order to build whatever layout best meets the need.

.. _site_structure:

Site Structure
--------------

.. _required-pages:

Required Pages
##############

Despite the flexibility in the CMS, some pages must always exist for the site to function properly. A site without a homepage isn't very useful, for example. The following cms pages are required for the website to fully function. Deleting any of these pages, could have unintended consequences. Pages with the following ``slug`` must exist:

- ``home``
    This is the front page for the site. This page MUST be the topmost page in the tree structure.

- ``about`` 
    Shows "about us" information describing BAP.

- ``privacy``
    Displays the privacy policy.

- ``contact``
    Shows contact information with an email link.

Main Nav Pages
##############

Setting a page as a ``subpage`` of the ``home`` page automatically adds it to the main nav menu (the red bar in the upper right). By default the following pages exists as main navigation pages:

- ``join`` 
    Information about joining BAP.

- ``media``
    Selected videos and pictures for the organization pulled from BAP's `Flickr <http://flickr.com>`_ and `YouTube <http://youtube.com>`_ accounts. For pointers on handling media, see :ref:`media-management`

Modifying Pages
---------------

The quickest way to edit a page is by logging in and using the ``Edit this page`` link found in the footer of all editable pages. You're then taken to a form allowing the modification of the page content, title and url. 

Page Editing
############

``Title``
	The ``Title`` field is the name that shows up in automatically generated menus/links and in your browser's title bar when you visit that page. 

``slug``
	A ``slug`` is a short identifier for the page that will be used in the url for the page. For example, a page with the slug of ``winter-meeting`` might be located at a url like http://iubap.org/p/winter-meeting/

``status``
	The ``Status`` controls whether or not the page appears to normal users.
	- Hidden pages don't appear in navigation menus, but are viewable if you go directly to their url
	- Draft pages are completely invisible to normal users. Use this status if you're not quite finished with a page and want to do some more work on it before people see it.
	- Published pages show up in menus and are viewable by everyone.

``template``
	TODO

``Redirect to``
	TODO

``Content``
	TODO

`Sandbox <http://pagesdemo.piquadrat.ch/admin/>`_ for testing

Arranging Pages
###############

Discuss ordering pages and moving them around. Also sub-pages.

LINK TO TUTORIAL

