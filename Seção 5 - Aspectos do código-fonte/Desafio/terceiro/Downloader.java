...
public class Downloader {	
	
	public static String [] URLs = new String[] {
			'http://servera/api/status',
	        'http://serverb/api/status',
	        'http://serverc/api/status',
	        'http://serverd/api/status',
	        'http://servere/api/status'
			};
	}
	public static List<String> resultados = new ArrayList<String>();	
	
	public static void addData(String resultado) {
		synchronized(Downloader.class) {
			resultados.add(resultado);
		}
	}
	
	public static List<String> checkStatus(int threadCount){
		try {
				for (int i = 0; i < 5; i++) {
					new ThreadDownload().start(resultados.get(i));
				return resultados;
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static class ThreadDownload extends Thread{
		private String url;
		public ThreadDownload(String url) {
			this.url = url;
		}
	
		@Override
		public void run(){
			try {
				URL url = new URL(url);
				HttpURLConnection conn = (HttpURLConnection) url.openConnection();
				conn.setConnectTimeout(5000);
				conn.setReadTimeout(5000);
				if (conn.getResponseCode()==200) {
					InputStream inputStream = conn.getInputStream();
			        BufferedReader in = new BufferedReader(new InputStreamReader(
                            inputStream));
			        String inputLine;
			        StringBuilder sb = new StringBuilder();
			        while ((inputLine = in.readLine()) != null) 
			        	sb.append(inputLine);
			        in.close();
					inputStream.close();
					conn.disconnect();
					Downloader.addData(sb.toString());
				}else{
					System.out.println("Server response code:"+conn.getResponseCode());
				}
			} catch (MalformedURLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	...
}
