import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-web",
    description="Meta package for oca-web Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-help_online',
        'odoo10-addon-support_branding',
        'odoo10-addon-web_access_rule_buttons',
        'odoo10-addon-web_action_conditionable',
        'odoo10-addon-web_advanced_search_wildcard',
        'odoo10-addon-web_advanced_search_x2x',
        'odoo10-addon-web_chatter_paste',
        'odoo10-addon-web_ckeditor4',
        'odoo10-addon-web_confirm_window_close',
        'odoo10-addon-web_decimal_numpad_dot',
        'odoo10-addon-web_dialog_size',
        'odoo10-addon-web_domain_field',
        'odoo10-addon-web_drop_target',
        'odoo10-addon-web_editor_background_color',
        'odoo10-addon-web_environment_ribbon',
        'odoo10-addon-web_export_view',
        'odoo10-addon-web_favicon',
        'odoo10-addon-web_fullscreen',
        'odoo10-addon-web_hide_db_manager_link',
        'odoo10-addon-web_ir_actions_act_window_message',
        'odoo10-addon-web_ir_actions_act_window_page',
        'odoo10-addon-web_listview_invert_selection',
        'odoo10-addon-web_listview_range_select',
        'odoo10-addon-web_m2x_options',
        'odoo10-addon-web_menu_navbar_needaction',
        'odoo10-addon-web_no_bubble',
        'odoo10-addon-web_notify',
        'odoo10-addon-web_readonly_bypass',
        'odoo10-addon-web_responsive',
        'odoo10-addon-web_search_autocomplete_prefetch',
        'odoo10-addon-web_search_with_and',
        'odoo10-addon-web_searchbar_full_width',
        'odoo10-addon-web_send_message_popup',
        'odoo10-addon-web_sheet_full_width',
        'odoo10-addon-web_shortcut',
        'odoo10-addon-web_switch_company_warning',
        'odoo10-addon-web_timeline',
        'odoo10-addon-web_translate_dialog',
        'odoo10-addon-web_tree_dynamic_colored_field',
        'odoo10-addon-web_tree_image',
        'odoo10-addon-web_tree_many2one_clickable',
        'odoo10-addon-web_widget_bokeh_chart',
        'odoo10-addon-web_widget_char_switchcase',
        'odoo10-addon-web_widget_color',
        'odoo10-addon-web_widget_darkroom',
        'odoo10-addon-web_widget_digitized_signature',
        'odoo10-addon-web_widget_domain_v11',
        'odoo10-addon-web_widget_float_formula',
        'odoo10-addon-web_widget_image_download',
        'odoo10-addon-web_widget_image_webcam',
        'odoo10-addon-web_widget_many2many_tags_multi_selection',
        'odoo10-addon-web_widget_mermaid',
        'odoo10-addon-web_widget_slick',
        'odoo10-addon-web_widget_slick_example',
        'odoo10-addon-web_widget_slickroom',
        'odoo10-addon-web_widget_text_markdown',
        'odoo10-addon-web_widget_timepicker',
        'odoo10-addon-web_widget_x2many_2d_matrix',
        'odoo10-addon-web_x2many_delete_all',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
