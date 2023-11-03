import java.io.File;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;

public class main {
    public static void main(String[] args) {
        try {
            // Parse the input XML file
            File inputFile = new File("group.xml");
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse(inputFile);

            // Get the student elements
            NodeList studentList = document.getElementsByTagName("student");
            for(int i = 0; i < studentList.getLength(); i++) {
                Element student = (Element) studentList.item(i);

                System.out.print("Student: " + i + " | ");

                // Get the average element
                Element average = (Element) student.getElementsByTagName("average").item(0);

                // Check the average mark value
                int averageMark = Integer.parseInt(average.getTextContent());

                NodeList other_nodes = student.getChildNodes();

                int averageFromNode = 0;
                int subjectCount = 0;

                for(int a = 0; a < other_nodes.getLength(); a++) {
                    Node child = other_nodes.item(a);

                    if(child.getNodeName() == "subject") {
                        NamedNodeMap attributes;
                        attributes = child.getAttributes();

                        averageFromNode += Integer.parseInt(attributes.getNamedItem("mark").getNodeValue());

                        subjectCount++;
                    }
                }

                // System.out.println(averageFromNode);
                // System.out.println(subjectCount);

                if(subjectCount > 0) {
                    averageFromNode = averageFromNode / subjectCount;
                }

                if(averageMark != averageFromNode) {
                    // Correct the average mark value
                    average.setTextContent(Integer.toString(averageFromNode));
                    System.out.println("Corrected.");
                } else {
                    System.out.println("Passed.");
                }
            }

            File outputFile = new File("output.xml");
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(document);
            StreamResult result = new StreamResult(outputFile);
            transformer.transform(source, result);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}