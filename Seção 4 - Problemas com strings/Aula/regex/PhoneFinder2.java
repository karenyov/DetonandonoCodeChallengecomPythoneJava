package s4;
import java.util.List;
import java.util.regex.MatchResult;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class PhoneFinder2 {
	private List<String> find(String texto) {
		return Pattern.compile("\\(\\d{2}\\)\\s*\\d{3,4}-\\d{4}")
				.matcher(texto)
				.results()
				.map(MatchResult::group)
				.collect(Collectors.toList());
	}
	public static void main(String [] args) {
		String texto="Os nossos telefones de contato são: "
				+ "(21) 324-2233 ou (22)3411-3311 - "
				+ "os telefones são fictícios!";
		PhoneFinder2 pf = new PhoneFinder2();
		System.out.println(pf.find(texto));
	}
}
