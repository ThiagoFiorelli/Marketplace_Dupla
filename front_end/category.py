from back_end.models.category import Category
from back_end.controller.ctrl_category import CategoryController
from flask import Blueprint, render_template, request, redirect

category = Blueprint(__name__, 'category')
CONTROLLER = CategoryController()
titulo_head = 'Lojinha'


@category.route('/cadastrar_categoria')
def cadastro_Categoria():
    mensagem = ''
    category_name = request.args.get('name')

    if category_name is not None:
        category_description = request.args.get('description')
        cat = Category(category_name, category_description)
        CONTROLLER.save(cat)
        mensagem = f'{category_name} cadastrado com sucesso'
    return render_template('create_category.html', menssagem=mensagem, titulo='Cadastro de Categorias', titulo_head=titulo_head)


@category.route('/listar_categorias')
def lista_categorias():
    list_cat = CONTROLLER.read_all()
    return render_template('list_categories.html', categories=list_cat, titulo="Categorias", titulo_head=titulo_head)


@category.route('/deletar_categoria/<identifier>')
def delete_category(identifier):
    category = CONTROLLER.read_by_id(identifier)
    CONTROLLER.delete(category)
    return redirect('/listar_categorias')


@category.route('/alterar_categoria/<identifier>', methods=['GET', 'POST'])
def altera_categorias(identifier):
    obj_cat = CONTROLLER.read_by_id(identifier)
    if request.method == 'POST':
        cat_name = request.form.get('name')
        cat_desc = request.form.get('description')
        obj_cat.name = cat_name
        obj_cat.description = cat_desc
        CONTROLLER.save(obj_cat)
        return redirect('/listar_categorias')
    return render_template('create_category.html', identifier=identifier, titulo='Alteração de Categoria', titulo_head=titulo_head, obj=obj_cat)