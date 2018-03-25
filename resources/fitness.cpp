int calc_fitness()
{
	for (int i=0; i<TAM_POP; i++)
	{
		pop[i][2] = ((sin(pow(pop[i][0],3))+sin(pow(pop[i][0],2))
					  +sin(pop[i][1]))*3)
					  +(sqrt((pow(pop[i][0],2)
					  +pow(pop[i][1],2))));
	}
	return 0;
}