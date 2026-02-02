package com.example.demo;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By.ByXPath;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activtiy4 {
    public static void main(String[] args) {
        WebDriver driver=new FirefoxDriver();
        driver.get("https://training-support.net/webelements/target-practice");
        System.out.println(driver.getTitle());
        System.out.println(driver.findElement(By.xpath("//h3[@class='text-3xl font-bold text-orange-600']")).getText());
        WebElement e1=driver.findElement(By.xpath("//h5[@class='text-3xl font-bold text-purple-600']"));
        System.out.println(e1.getCssValue("color"));
        WebElement e2=driver.findElement(By.className("bg-purple-200"));
        System.out.println(e2.getAttribute("class"));
        System.out.println(driver.findElement(By.className("bg-slate-200")).getText());
        driver.quit();
        
    }
    
}
