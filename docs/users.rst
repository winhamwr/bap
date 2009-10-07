.. _user-management:

**********************
Managing User Accounts
**********************

The IU BAP website integrates user account authorization with IU's `CAS <http://indiana.edu/kb/CAS>`_ system, which alleviates the need to actually create accounts for all users and manage their passwords. Users still need to be managed in the sense of giving certain people as members or faculty and giving some people permissions to perform certain actions (eg. editing site content or managing users). Almost all user account management takes place on via the User Management page at :menuselection:`Admin --> Users`

.. Note:
	Because CAS doesn't provide a way to query for existing users, only users that have logged in to the site at least once will exist in the user management interface. It is possible to create an account using the proper username, however, and that account will be tied to the CAS user the first time they do log in.

.. _user-permissions:

User Permissions (via ``groups``)
=================================

User permissions are controlled primarily by adding them to a group. This is more manageable than adding individual permissions to specific users and less prone to error. It also allows us to easily classify and sort users according to group.

.. _user-permissions-groups:

Groups
------

``BAP Member``
	BAP members are IU users that are actually members of the organization. Adding users to this group ensures that they appear on the :ref:`members-list` and that they're allowed to perform :ref:`event-sign-up`.

``BAP Faculty``
	As the name emplies, associated faculty should be members of this group. They'll then appear in the :ref:`faculty-list`.

``BAP Content Editor``
	Users that should be able to add, edit and delete site pages should be members of this group. In order to actually perform changes, they must also have the ``staff`` box checked.

``BAP User Administrator``
	Members of this group have permission to modify other users' accounts. It's important that only trusted and trained users have this ability. In order to actually make modification, the user must also have the ``staff`` box checked.

``BAP Event Attendance Admin``
	Users that should be able to manually modify event attendance, run attendance reports on other users and start the event signup page. These users must be marked as ``staff`` to manually alter the attendance record.

User Passwords
==============

Because user authentication is handled through the CAS system, the password settings via the user management pages don't actually do anything. The only way to change a password is for the user to handle the change via the IU user account system.

Access for People Without IU User Accounts
==========================================

It's not currently well-supported, but it's possible for users without an IU account to gain access to the members section. To do this, create an account for the person and then set a password for them through the password change form. They'll then be able to login via the `Admin Login <http://iubap.org/admin>`_, after which, they'll be able to visit the home page and access members-only functionality.

