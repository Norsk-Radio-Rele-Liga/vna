<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,1053,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=lavpassfilter.dat>
  <DataDisplay=lavpassfilter.dpl>
  <OpenDisplay=1>
  <Script=lavpassfilter.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <L L1 1 680 210 -26 10 0 0 "1 uH" 1 "" 0>
  <GND * 1 570 300 0 0 0 0>
  <GND * 1 800 300 0 0 0 0>
  <GND * 1 420 310 0 0 0 0>
  <GND * 1 920 310 0 0 0 0>
  <C C1 1 800 270 17 -26 0 1 "400 pF" 1 "" 0 "neutral" 0>
  <Pac P1 1 420 280 18 -26 0 1 "1" 1 "50 Ohm" 1 "0 dBm" 0 "1 GHz" 0 "26.85" 0>
  <Pac P2 1 920 280 18 -26 0 1 "2" 1 "50 Ohm" 1 "0 dBm" 0 "1 GHz" 0 "26.85" 0>
  <C C2 1 570 270 17 -26 0 1 "390 pF" 1 "" 0 "neutral" 0>
  <Eqn Eqn1 1 630 390 -30 16 0 0 "dBs21=dB(S[2,1])" 1 "dBs43=dB(S[4,3])" 1 "yes" 0>
  <.SP SP1 1 430 370 0 64 0 0 "lin" 1 "1 MHz" 1 "30 MHz" 1 "600" 1 "no" 0 "1" 0 "2" 0 "no" 0 "no" 0>
</Components>
<Wires>
  <710 210 800 210 "" 0 0 0 "">
  <800 210 800 240 "" 0 0 0 "">
  <570 210 650 210 "" 0 0 0 "">
  <570 210 570 240 "" 0 0 0 "">
  <420 210 420 250 "" 0 0 0 "">
  <420 210 570 210 "" 0 0 0 "">
  <920 210 920 250 "" 0 0 0 "">
  <800 210 920 210 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
