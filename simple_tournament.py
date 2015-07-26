import axelrod
strategies = [s() for s in axelrod.basic_strategies]
tournament = axelrod.Tournament(strategies)
results = tournament.play()
plot = axelrod.Plot(results)
p = plot.boxplot()
p.show()
