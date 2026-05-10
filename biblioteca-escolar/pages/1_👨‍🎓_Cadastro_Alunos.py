import streamlit as st
from banco import cadastrar_aluno


st.title('Cadastro de Alunos')


nome = st.text_input('Nome')
turma = st.text_input('Turma')
rm = st.text_input('RM')


if st.button('Cadastrar Aluno'):
    cadastrar_aluno(nome, turma, rm)
    st.success('Aluno cadastrado com sucesso!')
