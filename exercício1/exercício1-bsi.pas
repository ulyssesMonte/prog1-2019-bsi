Program Pzim ;
	var
		x:integer;
	Begin
		writeln('Digite um n�mero ');
		readln(x);
		if ((x mod 2)=0) then
			begin
				writeln('PAR');
			end
		else
			begin
				writeln('IMPAR');
			end;     
End.