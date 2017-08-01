#! /usr/bin/python2.7
# -*- coding: utf8 -*-

import datetime
# from plugin_ajaxselect import AjaxSelect

if 0:
    from gluon import db, Field, auth, IS_EMPTY_OR, IS_IN_DB, current, URL
    response = current.response

response.files.insert(5, URL('static',
                      'plugin_ajaxselect/plugin_ajaxselect.js'))
#response.files.append(URL('static', 'plugin_ajaxselect/plugin_ajaxselect.css'))
response.files.append(URL('static', 'plugin_listandedit/plugin_listandedit.css'))

db.define_table('genres',
    Field('genre', 'string'),
    format='%(genre)s')

db.define_table('biblical_figures',
    Field('figure', 'string'),
    format='%(figure)s')

db.define_table('docs',
    Field('name'),
    Field('filename'),
    Field('editor', 'list:reference auth_user'),
    Field('editor2', 'list:reference auth_user'),
    Field('editor3', 'list:reference auth_user'),
    Field('editor4', 'list:reference auth_user'),
    Field('assistant_editor', 'list:reference auth_user'),
    Field('assistant_editor2', 'list:reference auth_user'),
    Field('assistant_editor3', 'list:reference auth_user'),
    Field('proofreader', 'list:reference auth_user'),
    Field('proofreader2', 'list:reference auth_user'),
    Field('proofreader3', 'list:reference auth_user'),
    Field('version', 'double'),
    Field('introduction', 'text'),
    Field('provenance', 'text'),
    Field('themes', 'text'),
    Field('status', 'text'),
    Field('manuscripts', 'text'),
    Field('bibliography', 'text'),
    Field('corrections', 'text'),
    Field('sigla', 'text'),
    Field('copyright', 'text'),
    Field('citation_format', 'text'),
    Field('genres', 'list:reference genres'),
    Field('figures', 'list:reference biblical_figures'),
    format='%(name)s')
db.docs.editor.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                               db.auth_user._format,
                                               multiple=True))
db.docs.editor2.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                               db.auth_user._format,
                                               multiple=True))
db.docs.editor3.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                               db.auth_user._format,
                                               multiple=True))
db.docs.editor4.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                               db.auth_user._format,
                                               multiple=True))
#db.docs.editor.widget = lambda field, value: AjaxSelect(field, value,
                                                        #indx=1,
                                                        #multi='basic',
                                                        #lister='simple',
                                                        #sortable=True,
                                                        #orderby='last_name',
                                                        #).widget()
db.docs.assistant_editor.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                                         db.auth_user._format,
                                                         multiple=True))
db.docs.assistant_editor2.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                                         db.auth_user._format,
                                                         multiple=True))
db.docs.assistant_editor3.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                                         db.auth_user._format,
                                                         multiple=True))
#db.docs.assistant_editor.widget = lambda field, value: AjaxSelect(field, value,
                                                        #indx=2,
                                                        #multi='basic',
                                                        #lister='simple',
                                                        #sortable=True,
                                                        #orderby='last_name',
                                                        #).widget()
db.docs.proofreader.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                                    db.auth_user._format,
                                                    multiple=True))
db.docs.proofreader2.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                                    db.auth_user._format,
                                                    multiple=True))
db.docs.proofreader3.requires = IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id',
                                                    db.auth_user._format,
                                                    multiple=True))
#db.docs.proofreader.widget = lambda field, value: AjaxSelect(field, value,
                                                             #indx=3,
                                                             #multi='basic',
                                                             #lister='simple',
                                                             #sortable=True,
                                                             #orderby='last_name',
                                                             #).widget()
db.docs.genres.requires = IS_EMPTY_OR(IS_IN_DB(db, 'genres.id',
                                             db.genres._format,
                                             multiple=True))
db.docs.figures.requires = IS_EMPTY_OR(IS_IN_DB(db, 'biblical_figures.id',
                                                db.biblical_figures._format,
                                                multiple=True))

db.define_table('biblio',
    Field('record'),
    format='%(record)s')

db.define_table('pages',
    Field('page_label', 'string'),
    Field('title', 'string'),
    Field('body', 'text'),
    Field('poster', db.auth_user, default=auth.user_id),
    Field('post_date', 'datetime', default=datetime.datetime.utcnow()),
    format='%(title)s')

db.define_table('bugs',
    Field('title'),
    Field('body', 'text'),
    Field('poster', db.auth_user, default=auth.user_id),
    Field('post_date', 'datetime'),
    format='%(title)s')
