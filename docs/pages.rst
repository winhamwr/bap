.. _pages:

************************
Controlling Site Content
************************

The BAP Website uses a `Content Management System (CMS) <http://en.wikipedia.org/wiki/Content_management_system>`_ to allow users to edit content on specific pages with their browser. It's also possible to lay out pages in a hierarchy and to make links between pages in order to build whatever layout best meets the need.

.. _site-structure:

Site Structure
==============

.. _required-pages:

Required Pages
--------------

Despite the flexibility in the CMS, some pages must always exist for the site to function properly. A site without a homepage isn't very useful, for example. The following cms pages are required for the website to fully function. Deleting any of these pages, could have unintended consequences. Pages with the following ``slug`` must exist:

- ``home``
    This is the front page for the site. This page MUST be the topmost page in the tree structure.

- ``about`` 
    Shows "about us" information describing BAP.

- ``privacy``
    Displays the privacy policy.

- ``contact``
    Shows contact information with an email link.

.. _main-nav-pages:

Main Nav Pages
--------------

Setting a page as a ``subpage`` of the ``home`` page automatically adds it to the main nav menu (the red bar in the upper right). By default the following pages exists as main navigation pages:

- ``join`` 
    Information about joining BAP.

- ``media``
    Selected videos and pictures for the organization pulled from BAP's `Flickr <http://flickr.com>`_ and `YouTube <http://youtube.com>`_ accounts. For pointers on handling media, see :ref:`media-management`

.. _modifying-pages:

Modifying Pages
===============

The quickest way to edit a page is by logging in and using the ``Edit this page`` link found in the footer of all editable pages. You're then taken to a form allowing the modification of the page content, title and url. It's also possible to edit pages via :menuselection: `Admin --> Pages`

For a tutorial on basic page management and editing, see :ref:`pages-tutorial`

.. _page-editing:

Page Editing
------------

``Title``
	The ``Title`` field is the name that shows up in automatically generated menus/links and in your browser's title bar when you visit that page. 

``Slug``
	A ``slug`` is a short identifier for the page that will be used in the url for the page. For example, a page with the slug of ``winter-meeting`` might be located at a url like http://iubap.org/p/winter-meeting/

``Status``
	The ``Status`` controls whether or not the page appears to normal users.
	- ``Hidden`` pages don't appear in navigation menus, but are viewable if you go directly to their url
	- ``Draft`` pages are completely invisible to normal users. Use this status if you're not quite finished with a page and want to do some more work on it before people see it.
	- ``Published`` pages show up in menus and are viewable by everyone.

``Template``
	The page template defines what kind of content you're able to modify. Different templates result in different page layouts and allow you to insert content in different places. The ``default`` template defines just one main content area in the center of the page, while other templates might include things like an events calendar or a sidebar.

``Redirect to``
	If a value is chosen in this field, then visiting this page will automatically redirect the user to the value chosen. Generally, you won't use this field, but if you ever need to replace a page with another page, this is useful. For example, if you'd no longer like visitors to see the 2008 Career Fair page (because it's 2009), but you'd still like to keep that page around just in case, you could set the career fair 2008 page to redirect to the 2009 page. Any user that might have had the 2008 page bookmarked will then be automatically taken to the 2009 page.

``Content Blocks``
	Depending on the ``Template`` chosen, there are one or more content fields with different names. These allow you to define exactly what text/images/links etc appear in a particular position on a page. For example, the default template has just one ``body content`` block that defines what appears in the center of the page.

.. Note:

If you'd like to practice making, moving and deleting pages, you can use the `Sandbox <http://pagesdemo.piquadrat.ch/admin/>`_ for testing. It won't effect the actual site at all, so it's a worry-free way of practicing.

.. _arranging-pages:

Arranging Pages
---------------

To aid organization, pages are arranged in a tree structure. You can view the structure via :menuselection: `Admin --> Pages`. By clicking the ``move`` button next to a page, you're able to select one of ``move down``, ``move up``, ``move in`` and ``move out``. This allows you to change the page order on the same level and also change the nesting of pages. The navigation menu in the upper right automatically displays links to all child pages (pages that are nested inside another page), so by nesting pages, you're able to build navigation menus that logically link sections of the site together.

