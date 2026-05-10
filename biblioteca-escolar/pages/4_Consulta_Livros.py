import streamlit as st
from banco import listar_livros


st.title('Consulta de Livros')


livros = listar_livros()


for livro in livros:
    st.write(f'ID: {livro[0]}')
    st.write(f'Título: {livro[1]}')
    st.write(f'Autor: {livro[2]}')
    st.write(f'Categoria: {livro[3]}')
    st.write(f'Quantidade: {livro[4]}')
    st.write('----------------------')
