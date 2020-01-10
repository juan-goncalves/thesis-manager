from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('personas', views.person_index, name='person_index'),
    path('personas/agregar', views.PersonDataCreate.as_view(), name='create_person'),
    path('personas/tipos', views.person_type_index, name='person_type_index'),
    path('tg/agregar', views.ThesisCreate.as_view(), name='create_thesis'),
    path('tg/estados', views.thesis_status_index, name='thesis_status_index'),
    path('personas/tipos/agregar', views.PersonTypeCreate.as_view(), name='create_person_type'),
    path('tg/estados/agregar', views.ThesisStatusCreate.as_view(), name='create_thesis_status'),
    path('personas/tipos/<int:pk>/editar', views.PersonTypeUpdate.as_view(), name='edit_person_type'),
    path('personas/agregar', views.PersonDataCreate.as_view(), name='create_person'),
    path('personas/<str:pk>', views.person_detail, name='person_detail'),
    path('personas/<str:pk>/editar', views.PersonDataUpdate.as_view(), name='edit_person'),
    path('defensas/', views.defence_index, name='defence_index'),
    path('defensas/pendientes', views.pending_defence_index, name='pending_defence_index'),
    path('defensas/agregar', views.DefenceCreate.as_view(), name='create_defence'),
    path('jurado/agregar', views.JuryCreate.as_view(), name='create_jury'),
    path('jurado/<int:pk>/editar', views.JuryUpdate.as_view(), name='update_jury'),
    path('jurado/<int:pk>/eliminar', views.JuryDelete.as_view(), name='delete_jury'),
    path('defensas/<str:pk>/editar', views.DefenceUpdate.as_view(), name='update_defence'),
    path('tg', views.thesis_index, name='thesis_index'),
    path('tg/historico', views.thesis_historic_index, name='thesis_historic_index'),
    path('tg/historico/<str:pk>', views.thesis_historic_detail, name='thesis_historic_detail'),
    path('tg/<str:pk>', views.thesis_detail, name='thesis_detail'),
    path('tg/<str:pk>/editar', views.ThesisUpdate.as_view(), name='edit_thesis'),
    path('tg/estados/<int:pk>/editar', views.ThesisStatusUpdate.as_view(), name='edit_thesis_status'),
    path('person-type-autocomplete', views.PersonTypeAutoComplete.as_view(), name='person-type-autocomplete'),
    path('proposal-autocomplete', views.ProposalAutocomplete.as_view(), name='proposal-autocomplete'),
    path('term-autocomplete', views.TermAutocomplete.as_view(), name='term-autocomplete'),
    path('thesis-autocomplete', views.ThesisAutocomplete.as_view(), name='thesis-autocomplete'),
    path('teacher-autocomplete', views.TeacherAutoComplete.as_view(), name='teacher-autocomplete'),
    path('student-autocomplete', views.StudentAutoComplete.as_view(), name='student-autocomplete'),
    path('personas/<str:person_id_card_number>', views.person_detail, name='person_detail'),
    path('propuestas', views.proposal_index, name='proposal_index'),
    path('propuestas/agregar', views.ProposalCreate.as_view(), name='create_proposal'),
    path('propuestas/<str:pk>/editar', views.ProposalEdit.as_view(), name='edit_proposal'),
    path('term', views.term_index, name='term_index'),
    path('term/agregar', views.TermCreate.as_view(), name='create_term'),
    path('term/<int:pk>/editar', views.TermUpdate.as_view(), name='edit_term'),
    path('estatus_propuestas', views.proposal_status_index, name='proposal_status_index'),
    path('estatus_propuestas/agregar', views.ProposalStatusCreate.as_view(), name='create_proposal_status'),
    path('estatus_propuestas/<str:pk>/editar', views.ProposalStatusUpdate.as_view(), name='edit_proposal_status'),
    path('estadisticas', views.stats_view, name='stats_view'),
    path('propuestas_no_aprobadas', views.proposal_not_approved_list, name='proposal_not_approved_list'),
    path('propuestas/<str:pk>', views.proposal_detail, name='proposal_detail'),
    path('propuestas-pdf', views.ProposalPdf.as_view(), name='proposal_pdf'),
    path('propuestas-no-aprobadas-pdf', views.ProposalNotApprovedPdf.as_view(), name='proposal_not_approved_pdf'),
    path('personas-pdf', views.PersonsListPdf.as_view(), name='person_pdf'),
]
