# newdisc

## Objetivo

Este projeto tem como objetivo criar um ambiente mais flexível e de fácil personalização para distribuição do sistema de análise comportamental da ouzaz.

## Estrutura

O projeto está distribuído da seguinte forma:

**Front**: A pasta front contém os fonts do frontend principal, que aplica o teste e exibe seu resultado. Ele foi desenvolvido em React.JS.

**Back**: Essa pasta contém os fonts do backend desenvolvido em Python, usando o framework FastAPI.

**Infra**: Toda infra está baseada na Cloud da Google (GCP): 

- Back hospedado no cloud run (serverless), como pacote Docker e tendo seus dados armazenados no firestore (Banco em Tempo Real, NoSQL do Firebase);

- Front: está hospedado no Hosting do Firebase.
