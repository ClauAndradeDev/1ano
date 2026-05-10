import streamlit as st
from banco import cadastrar_livro


st.title('Cadastro de Livros')


titulo = st.text_input('Título')
autor = st.text_input('Autor')
categoria = st.text_input('Categoria')
quantidade = st.number_input('Quantidade', min_value=1)


if st.button('Cadastrar Livro'):
    cadastrar_livro(titulo, autor, categoria, quantidade)
    st.success('Livro cadastrado com sucesso!')
