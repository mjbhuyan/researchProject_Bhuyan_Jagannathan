package test.es.unizar.disco.dice.profile.tests;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.Collections;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.uml2.uml.Model;



public abstract class AbstractTest {

		public static ResourceSet resourceSet;


		public static Model loadUMLModel(String modelpath) throws IOException{
			final URI modelURI = URI.createFileURI(
					Paths.get("src/test/resources/" +modelpath + ".uml" )
							.toFile().getAbsolutePath());
			System.out.println("umlModelURI is: " + modelURI);
			return (Model) loadResourceFromUri(modelURI); 
			
		}
		
		protected static EObject loadResourceFromUri(URI theURI) throws IOException {
			Resource theResource = getResourceSet().getResource(theURI, true);
			theResource.load(Collections.EMPTY_MAP);
			return theResource.getContents().get(0);
		}

		protected static synchronized ResourceSet getResourceSet() {

			if (resourceSet == null) {
				resourceSet = new ResourceSetImpl();
			}
			return resourceSet;
		}
	
}
