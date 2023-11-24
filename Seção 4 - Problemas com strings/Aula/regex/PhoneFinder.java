package s4;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PhoneFinder {
	private List<String> find(String texto) {
		Pattern pattern = Pattern.compile("\\(\\d{2}\\)\\s*\\d{3,4}-\\d{4}");
		Matcher matcher = pattern.matcher(texto);
		List<String> encontrados = new ArrayList<String>();
		while (matcher.find()) {
			encontrados.add(matcher.group());
		}
		return encontrados;
	}
	public static void main(String [] args) {
		String texto="Os nossos telefones de contato são: "
				+ "(21) 324-2233 ou (22)3411-3311 - "
				+ "os telefones são fictícios!";
		PhoneFinder pf = new PhoneFinder();
		System.out.println(pf.find(texto));
	}
}
