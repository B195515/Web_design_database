import java.io.*;
import java.math.BigDecimal;
import java.math.RoundingMode;
import javax.vecmath.Point3d;
import java.util.Hashtable;
import java.util.Map;
import java.util.ArrayList;
// import CDK class
import org.openscience.cdk.Molecule;
import org.openscience.cdk.DefaultChemObjectBuilder;
import org.openscience.cdk.io.iterator.IteratingMDLReader;
import org.openscience.cdk.io.MDLReader;
import org.openscience.cdk.interfaces.*;
import org.openscience.cdk.smiles.*;
import org.openscience.cdk.qsar.descriptors.molecular.WHIMDescriptor;
import org.openscience.cdk.qsar.DescriptorValue;
import org.openscience.cdk.qsar.result.*;
import org.openscience.cdk.CDKConstants;
public class SDF_smiles {
    
    // This program will start from here
    public static void main(String args[]) {
        if (args.length != 1) {
	    // Wrong arguments output message
	    System.out.println("Usage: java SDF_smiles sdffile");
	    System.exit(0);
        }
        //String for SDfile Multi-SDFile allowed
	String SDFile = args[0];
	FileReader fr = null;
	BufferedReader br = null;
	// get molecule object using CDK
        System.setProperty("java.util.Arrays.useLegacyMergeSort", "true");
	try{
	    IteratingMDLReader MDLReader = new IteratingMDLReader(new FileInputStream(SDFile), DefaultChemObjectBuilder.getInstance());
	    while (MDLReader.hasNext()){
		//(Molecule)MDLReader.next() to get a molecule object
		//total_distance = cd.get3DWienerIndex((Molecule)MDLReader.next());
                Molecule mymol;
                mymol = (Molecule)MDLReader.next();
		String Name = "";
                SmilesGenerator smg = new SmilesGenerator();
		Name = new String(String.valueOf(mymol.getProperty(CDKConstants.TITLE)));
		System.out.format("%s %s %n",Name,smg.createSMILES(mymol));
	    }
	}catch(Exception e){
	    System.out.println(e.toString());
	}
    }
}
