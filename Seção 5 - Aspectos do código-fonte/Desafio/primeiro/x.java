
...
public class x {
	public static tsect T = new tsect();
	private void mts(PL p, long a, SRL b) {
		List<Ks> l = new ArrayList<Ks>();
		for (Ks k : p) 
			if (k.p(a))
				l.add(k);
		for (Ks i : l)
			if (T.calc(i)>3.456)
				i.pst=1;
			else if (T.calc(i)<=3.456 && T.calc(i)>1.45) {
				i.pst=2;
				T.pl= false;
			}
	}
}
...
	x ep=new x();
...
	x.mts(pnl1,34,zx);
