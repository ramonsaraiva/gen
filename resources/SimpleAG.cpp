#include <time.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
 
#define TAM_POP 10
#define GENERATIONS 10
 
double PROB_MUT = 0.2;             // percentual (0..1)
double AG_RANGE = 20.0;            // teste com 1?
double AG_RANGE_OFFSET = 10.0;     // teste com 0?
 
/* Nesta estrutura, 0 e 1 sao as variaveis da funcao e
   2 eh usado para guardar o fitness */
 
float pop[TAM_POP][3];  
 
/* cria populacao */
 
int cria_populacao()
{
    for (int i=0; i<TAM_POP; i++)
    {
    //  pop[i][0] = (float) rand();  
    //  pop[i][1] = (float) rand();
     
    //pop[i][0] = (float) rand() / (float) RAND_MAX;
    //pop[i][1] = (float) rand() / (float) RAND_MAX;
     
    pop[i][0] = (((float) rand() / (float) RAND_MAX) * AG_RANGE) - AG_RANGE_OFFSET;
    pop[i][1] = (((float) rand() / (float) RAND_MAX) * AG_RANGE) - AG_RANGE_OFFSET;
     
    }
    return 0;
}
 
/* mostra populacao */
 
int mostra_populacao()
{
    for (int i=0; i<TAM_POP; i++)
    {
        printf("%d %.3f %.3f\n",i, pop[i][0],pop[i][1]);
    }
    return 0;
}
 
/* mostra populacao c fitness*/
 
int mostra_populacao_fitness()
{
    for (int i=0; i<TAM_POP; i++)
    {
        printf("%d %.3f %.3f fit: %.3f\n",i, pop[i][0],pop[i][1],pop[i][2]);
    }
    return 0;
}
 
/* calcula fitness */
 
int calc_fitness()
{
    for (int i=0; i<TAM_POP; i++)
    {
        pop[i][2] = (pop[i][0] * pop[i][0]) + (pop[i][1] * pop[i][1]);
    }
    return 0;
}
 
/* pega menor */
 
int pega_menor()
{
    float menor = (float) RAND_MAX;
    int indice_menor = 0;
 
    for (int i=0; i<TAM_POP; i++)
    {
        if (menor > pop[i][2])
        {
            menor = pop[i][2];
            indice_menor = i;
        }
    }
   
    return indice_menor;
}
 
/* cruzamento */
 
int cruzamento(int indice_menor)
{
    for (int i=0; i<TAM_POP; i++)
    {
        pop[i][0] = (pop[i][0] + pop[indice_menor][0]) / 2.0;
        pop[i][1] = (pop[i][1] + pop[indice_menor][1]) / 2.0;
    }
    return 0;
}
 
/* mutacoes */
 
int mutacao_unif_sem_elitismo()
{
    for (int i=0; i<TAM_POP; i++)
    {
        for (int j=0;j<2;j++)
        {
            float r = rand() / (float) RAND_MAX;
            if (r < PROB_MUT)
            {
                pop[i][j] = (((float) rand() / (float) RAND_MAX) * AG_RANGE) - AG_RANGE_OFFSET;
            }
        }
    }
       
    return 0;
}
 
int mutacao_unif_com_elitismo(int indice_menor)
{
    for (int i=0; i<TAM_POP; i++)
    {
        if (i != indice_menor)
        {
            for (int j=0;j<2;j++)
            {
                float r = rand() / (float) RAND_MAX;
                if (r < PROB_MUT)
                {
                    pop[i][j] = (((float) rand() / (float) RAND_MAX) * AG_RANGE) - AG_RANGE_OFFSET;
                }
            }
        }
    }
 
    return 0;
}
 
int mutacao_gauss_sem_elitismo()
{
    for (int i=0; i<TAM_POP; i++)
    {
        for (int j=0;j<2;j++)
        {
            float r = rand() / (float) RAND_MAX;
            if (r < PROB_MUT)
            {
                float q;
                q = rand() / (float) RAND_MAX;     // valor entre 0 e 1
                q = (q * 2.0) - 1.0;               // valor entre -1 e 1
                q = q / 4.0;                       // valor entre + 0.25 e -0.25
                q = 1.0 + q;                       // valor entre 0.75 e 1.25  
 
                pop[i][j] = pop[i][j] * q;
            }
        }
    }
 
    return 0;
}
 
int mutacao_gauss_com_elitismo(int indice_menor)
{
    for (int i=0; i<TAM_POP; i++)
    {
        if (i != indice_menor)
        {
            for (int j=0;j<2;j++)
            {
                float r = rand() / (float) RAND_MAX;
                if (r < PROB_MUT)
                {
                    float q;
                    q = rand() / (float) RAND_MAX;     // valor entre 0 e 1
                    q = (q * 2.0) - 1.0;               // valor entre -1 e 1
                    q = q / 4.0;                       // valor entre + 0.25 e -0.25
                    q = 1.0 + q;                       // valor entre 0.75 e 1.25  
 
                    pop[i][j] = pop[i][j] * q;
                }
            }
        }
    }
 
    return 0;
}
 
/* bloco principal */
 
int main()
{
    srand(time(NULL));      
 
    cria_populacao();
 
    printf("pop criada:\n");
    mostra_populacao();
    getchar();
 
    calc_fitness();
 
    printf("pop criada c fitness:\n");
    mostra_populacao_fitness();
    getchar();
 
    int g=1;  // discutir
 
    while (g<GENERATIONS)
    {
        //selecao
        int indice_menor = pega_menor();
           
        // cruzamento
        cruzamento(indice_menor);
 
        //mutacao
        //mutacao_unif_com_elitismo(indice_menor);
        //mutacao_unif_sem_elitismo();
        mutacao_gauss_com_elitismo(indice_menor);
        //mutacao_gauss_sem_elitismo();
 
        //calc_f
        calc_fitness();
 
        printf("geracao: %d \n\n",g);
        mostra_populacao_fitness();
       
        // apenas para view
        indice_menor = pega_menor();
        printf("\nBest: %d %.3f\n",indice_menor, pop[indice_menor][2]);
       
        getchar();
 
        g++;
    }
 
    printf("That's all, Folks!");
    getchar();
}
