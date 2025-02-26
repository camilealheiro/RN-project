# Detecção de Células Binucleadas com Micronúcleos usando Redes YOLO, Faster R-CNN e SSD

## Visão Geral
Este projeto tem como objetivo a detecção e classificação de células binucleadas com e sem micronúcleos em imagens microscópicas, utilizando três arquiteturas de redes neurais: YOLO, Faster R-CNN e SSD. As imagens foram capturadas manualmente no CRCN, usando um microscópio Leica DM 500, com resolução de 2048 × 1536 pixels.

## Estrutura do Projeto
O projeto está organizado em três pastas, cada uma contendo implementações das diferentes redes utilizadas:
- `YOLO/` - Implementação da rede YOLO para detecção e classificação
- `Faster_RCNN/` - Implementação da rede Faster R-CNN
- `SSD/` - Implementação da rede SSD

## Base de Dados
O conjunto de dados é composto por um total de 889 imagens, anotadas manualmente e validadas por citogenistas experientes seguindo o protocolo HUMN.

### Distribuição das Classes
- **Células binucleadas sem micronúcleo (BN):** 543 imagens
- **Células binucleadas com micronúcleo (BNMN):** 346 imagens

### Divisão do Conjunto de Dados
- **Treinamento:** 621 imagens (379 BN, 242 BNMN)
- **Teste:** 268 imagens (164 BN, 104 BNMN)

### Processamento das Imagens
- Descartadas imagens com baixa qualidade, sobreposição de núcleos ou danos ao citoplasma.
- Conversão do formato **TIFF** para **PNG** para melhor compatibilidade e armazenamento.
- Redimensionamento das imagens para os seguintes tamanhos:
  - 1080 × 1080
  - 720 × 720
  - 640 × 640

## Anotação das Classes
As imagens foram anotadas para classificação precisa nas seguintes categorias:
- **Células binucleadas sem micronúcleo**
- **Células binucleadas com micronúcleo**
- **Micronúcleos isolados**

## Avaliação de Desempenho
Para medir a eficácia dos modelos, utilizamos as seguintes métricas:
- **Precisão**
- **Recall**
- **mAP50** (Média de Precisão com IoU ≥ 50%)
- **mAP50-95** (Média de Precisão em várias faixas de IoU de 50% a 95%)

