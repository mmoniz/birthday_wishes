import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;

/**
 * 
 * @author Mike Moniz
 * 
 * An automated way of always wishing you're friends a happy birthday!
 *
 */
public class Happy {
    
	//change to your path chromedriver path
	private static final String driver_path = "C:\\Program Files (x86)\\Google\\chromedriver.exe";
	private static final String pass = "password";
	private static final String email = "email";
	
	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver", driver_path);
		
		ChromeDriver driver = new ChromeDriver();
		
		String message = "Happy birthday! :)";
		
		sendHappyBirthdayMessage(driver, message);
		
		driver.close();
        driver.quit();
	}
	
	private static void login(RemoteWebDriver driver, String email, String pass){
		try {// Log-in to Facebook
	        WebElement txtLogin    = driver.findElementByName("email");
	        WebElement txtPassword = driver.findElementByName("pass");
	
	        txtLogin.sendKeys(email);
	        txtPassword.sendKeys(pass);
	        txtPassword.sendKeys("\n");
		} catch (Exception e) {
			System.out.println("Couldn't login");
		}
	}
	
	private static void sendHappyBirthdayMessage(RemoteWebDriver driver, String message) {
		String birthday_url = "https://www.facebook.com/events/birthdays";
		driver.get(birthday_url);
		
		login(driver, Happy.email, Happy.pass);
		
		//Option 1: directly from the event page
		wishPeopleHappyBirthday(driver, birthday_url, message);
		
		//Option 2: via friend's wall
		//sendHappyBirthdayMessageByWall(driver, message);
				
	}
	
	private static void wishPeopleHappyBirthday(RemoteWebDriver driver,
			String birthday, String message) {

		try {
			List<WebElement> childs = driver.findElements(By.xpath("//*[@id=\"events_birthday_view\"]/div[1]/div[2]//*"));
	
	        for (WebElement child : childs) {
	        	if ( "textarea".equals(child.getTagName()) ) {
	        		child.sendKeys(message);
	        		child.submit();
	        	}
	        }
		} catch (Exception e) {
			System.out.println("Could not find birthday people");
		}
	}


	private static List<String> findBirthdayPeople(RemoteWebDriver driver) {
		ArrayList<String> urls = new ArrayList<String>();
		try {
			WebElement parent = driver.findElementByXPath("//*[@id=\"events_birthday_view\"]/div[1]/div[2]");
			
			List<WebElement> childs = parent.findElements(By.xpath(".//*"));
	
	        for (WebElement child : childs) {
	        	if ( "a".equals(child.getTagName()) ) {
	        		String link = child.getAttribute("href");
	        		if (link.indexOf("friendship") == -1){
	            		urls.add(link);
	            		System.out.println(link);
	        		}
	        	}
	        }
		} catch (Exception e) {
			System.out.println("Could not find birthday people");
		}
		return urls;
	}

	private static void sendHappyBirthdayMessageByWall(RemoteWebDriver driver, String message) {
		//Get the friends fb url
		List<String> birthdayPeople = findBirthdayPeople(driver);
		
		for (String url : birthdayPeople) {
			try {
				postToWall(driver, url, message);
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
	
	public static void postToWall(RemoteWebDriver driver, String url, String message) {
		try {
        	driver.get(url);
			Thread.sleep(1000);
		
	        WebElement parent = driver.findElementByClassName("fbTimelineComposerUnit");
	
	        List<WebElement> childs = parent.findElements(By.xpath(".//*"));
	
	        for (WebElement child : childs) {
	        	if ( "textarea".equals(child.getTagName()) ) {
	        		child.sendKeys(message);
	        		child.submit();
	        		break;
	        	}
	        }
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
