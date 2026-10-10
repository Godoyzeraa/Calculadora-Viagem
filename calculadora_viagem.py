def calcular_viagem():
    print("=" * 45)
    print("   CALCULADORA DE VIAGEM E COMPARATIVO DE COMBUSTÍVEL")
    print("=" * 45)

    try:
        # Entradas principais
        distancia = float(input("Digite a distância total da viagem (em km): "))
        pedagio = float(input("Valor total gasto com pedágios (R$ - digite 0 se não houver): "))

        print("\n--- DADOS DA GASOLINA ---")
        consumo_gasolina = float(input("Consumo médio com Gasolina (km/L): "))
        preco_gasolina = float(input("Preço do litro da Gasolina (R$): "))

        print("\n--- DADOS DO ETANOL ---")
        consumo_etanol = float(input("Consumo médio com Etanol (km/L): "))
        preco_etanol = float(input("Preço do litro do Etanol (R$): "))

        if distancia <= 0 or pedagio < 0 or consumo_gasolina <= 0 or preco_gasolina <= 0 or consumo_etanol <= 0 or preco_etanol <= 0:
            print("\n[Erro] Os valores de distância, consumo e preços devem ser maiores que zero.")
            return

        # --- CÁLCULOS DA PORCENTAGEM ---
        porcentagem_preco = (preco_etanol / preco_gasolina) * 100

        # --- CÁLCULOS GASOLINA ---
        litros_gasolina = distancia / consumo_gasolina
        custo_comb_gasolina = litros_gasolina * preco_gasolina
        custo_total_gasolina = custo_comb_gasolina + pedagio

        # --- CÁLCULOS ETANOL ---
        litros_etanol = distancia / consumo_etanol
        custo_comb_etanol = litros_etanol * preco_etanol
        custo_total_etanol = custo_comb_etanol + pedagio

        # --- EXIBIÇÃO DOS RESULTADOS ---
        print("\n" + "=" * 45)
        print("              RESULTADOS DA VIAGEM")
        print("=" * 45)
        
        print(f"\n📊 Relação de Preço: O Etanol custa {porcentagem_preco:.1f}% da Gasolina.")

        print("\n⛽ [GASOLINA]:")
        print(f"  - Litros necessários: {litros_gasolina:.2f} L")
        print(f"  - Custo total (com pedágio): R$ {custo_total_gasolina:.2f}")

        print("\n🌽 [ETANOL]:")
        print(f"  - Litros necessários: {litros_etanol:.2f} L")
        print(f"  - Custo total (com pedágio): R$ {custo_total_etanol:.2f}")

        print("\n" + "-" * 45)
        print("                  CONCLUSÃO")
        print("-" * 45)
        
        if custo_total_etanol < custo_total_gasolina:
            diferenca = custo_total_gasolina - custo_total_etanol
            print(f"✨ Compensa mais ir de **ETANOL**!")
            print(f"   Você economiza aproximadamente R$ {diferenca:.2f} nesta viagem.")
        elif custo_total_gasolina < custo_total_etanol:
            diferenca = custo_total_etanol - custo_total_gasolina
            print(f"✨ Compensa mais ir de **GASOLINA**!")
            print(f"   Você economiza aproximadamente R$ {diferenca:.2f} nesta viagem.")
        else:
            print("⚖️ Tanto faz! O custo total com ambos os combustíveis será exatamente o mesmo.")
        
        print("=" * 45)

    except ValueError:
        print("\n[Erro] Entrada inválida! Por favor, digite apenas números (use ponto para decimais, ex: 5.5).")

if __name__ == "__main__":
    calcular_viagem()