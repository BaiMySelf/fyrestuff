
public class RealTime {

	public static void main(String argsp[]) {
		
		for (int i = 0; i < 100; i++) {
			if (i < 10)
				System.out.println("0.00" + i + "00E-03,");
			else if (i < 100)
				System.out.println("0.0" + i + "00E-03,");
				
		}
		
		
		
	}
	
}
