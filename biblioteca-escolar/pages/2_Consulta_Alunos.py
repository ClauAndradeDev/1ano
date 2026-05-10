import streamlit as st
from banco import listar_alunos


st.title('Consulta de Alunos')


alunos = listar_alunos()


for aluno in alunos:
    st.write(f'ID: {aluno[0]}')
    st.write(f'Nome: {aluno[1]}')
    st.write(f'Turma: {aluno[2]}')
    st.write(f'RM: {aluno[3]}')
    st.write('----------------------')
