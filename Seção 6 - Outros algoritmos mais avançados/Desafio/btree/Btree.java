package s6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.SortedMap;
import java.util.TreeMap;

class Nodo {
	Nodo esquerdo;
	Integer valor;
	Nodo direito;
	@Override
	public String toString() {
		return "|" + this.esquerdo 
				+ ";" + this.valor + ";" 
				+ this.direito + "|";
	}
}

public class Btree {
	public Nodo construir (Integer [] V) {
		if (V.length==0) {
			return null;
		}
		int meio = (int) Math.ceil(V.length/2);
		Nodo nodo = new Nodo();
		nodo.valor=V[meio];
		nodo.esquerdo=construir(Arrays.copyOfRange(V, 0, meio));
		nodo.direito=construir(Arrays.copyOfRange(V, meio+1, V.length));
		return nodo;
	}
	private Nodo pesquisar(Nodo a, int valor) {
		if (a==null || a.valor.equals(valor)) {
			return a;
		}
		if (a.valor<valor) {
			return pesquisar(a.direito,valor);
		}
		return pesquisar(a.esquerdo,valor);
	}
	private Nodo ancestral(Nodo nodo, int ano1, int ano2) {
		if (nodo==null) {
			return null;
		}
		if (nodo.valor>Math.max(ano1,ano2)) {
			return ancestral(nodo.esquerdo,ano1,ano2);
		}
		else if (nodo.valor<Math.min(ano1, ano2)) {
			return ancestral(nodo.direito,ano1,ano2);
		}
		return nodo;
	}
	private void preordem(Nodo a, List<Integer> saida) {
		if (a != null) {
			saida.add(a.valor);
			preordem(a.esquerdo,saida);
			preordem(a.direito,saida);
		}
	}
	private static void emordem(Nodo a, List<Integer> saida) {
		if (a != null) {
			emordem(a.esquerdo,saida);
			saida.add(a.valor);
			emordem(a.direito,saida);
		}
	}
	private static void posordem(Nodo a, List<Integer> saida) {
		if (a != null) {
			posordem(a.esquerdo,saida);
			posordem(a.direito,saida);
			saida.add(a.valor);
		}
		
	}
	public static void main (String [] args) {
		SortedMap<Integer,String> lista = new TreeMap<Integer,String>();
	    lista.put(1958,"Brasil é campeão mundial de futebol na Suécia");
	    lista.put(1962,"Eleição do Papa Paulo VI");
	    lista.put(1954,"Primeiro transplante de órgão - Rim");
	    lista.put(1962,"Crise dos mísseis em Cuba");
	    lista.put(1951,"Getúlio Vargas assume seu segundo mandato de Presidente");
	    lista.put(1955,"Primeira vacina contra poliomielite");
	    lista.put(1960,"Inauguração de Brasília");
	    lista.put(1949,"Criação da OTAN");
	    lista.put(1959,"Criação da SUDENE");
	    lista.put(1952,"Detonação da primeira bomba de hidrogênio");
	    lista.put(1961,"Iuri Gagarin se torna o primeiro humano a ir ao espaço");
	    lista.put(1958,"Revolução Cubana");
	    lista.put(1963,"Lançamento do álbum de estréias do Beatles");
	    lista.put(1950,"Uruguai derrota o Brasil no Maracanã e se torna campeão mundial de futebol");
	    lista.put(1957,"Lançamento do primeiro satélite artificial - Sputnik");
	    lista.put(1956,"Elvis Presley lança seu primeiro álbum musical");
	    lista.put(1953,"Getúlio Vargas cria a Petrobras");
	    
	    Btree bt = new Btree();
	    Nodo a=bt.construir((Integer[]) lista.keySet().toArray(Integer[]::new));
	    System.out.println(bt.pesquisar(a,1954));
	    System.out.println(bt.pesquisar(a,1952));
	    System.out.println(lista.get(bt.ancestral(a, 1953, 1954).valor)); //"Primeiro transplante de órgão - Rim"
	    System.out.println(lista.get(bt.ancestral(a, 1958, 1963).valor)); //"Inauguração de Brasília"
	    List<Integer> saida=new ArrayList<Integer>();
	    bt.preordem(a,saida);
	    System.out.println("Pre-ordem: " + saida);
	    saida=new ArrayList<Integer>();
	    emordem(a,saida);
	    System.out.println("Em-ordem: " + saida); 
	    saida=new ArrayList<Integer>();
	    posordem(a,saida);
	    System.out.println("Pos-ordem: " + saida);	
	    
	    
	    lista = new TreeMap<Integer,String>();
	    lista.put(1,"fato 1");
	    lista.put(2,"fato 2");
	    lista.put(3,"fato 3");
	    lista.put(4,"fato 4");
	    lista.put(5,"fato 5");
	    lista.put(6,"fato 6");
	    lista.put(7,"fato 7");
	    a=bt.construir((Integer[]) lista.keySet().toArray(Integer[]::new));
	    System.out.println(bt.pesquisar(a,3));
	    System.out.println(bt.pesquisar(a,5));
	    System.out.println(lista.get(bt.ancestral(a, 5, 7).valor)); //"fato 6"
	    saida=new ArrayList<Integer>();
	    bt.preordem(a,saida);
	    System.out.println("Pre-ordem: " + saida); //[4, 2, 1, 3, 6, 5, 7]
	    saida=new ArrayList<Integer>();
	    emordem(a,saida);
	    System.out.println("Em-ordem: " + saida); //[1, 2, 3, 4, 5, 6, 7]
	    saida=new ArrayList<Integer>();
	    posordem(a,saida);
	    System.out.println("Pos-ordem: " + saida); //[1, 3, 2, 5, 7, 6, 4]
	}

}
