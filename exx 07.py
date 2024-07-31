l = float(input('Largura da parede: '))
A = float(input('altura da parede: '))
área = l*A
print('Sua parede tem a dimensão de {} x {} e área de {}m'.format(l, A, área))
tinta = área/2
print('Para sua parede ser pintada você precisara de {:.2f}L de tinta'
      .format(tinta))
