import org.python.util.PythonInterpreter
import org.python.core.*

class Python extends leikr.Engine{
	def interp = new PythonInterpreter();
	def cre, upd, ren
	
	PyFloat pf
	
	void create(){
		new File("Programs/Python/Code/Compiled/PythonShim.py").withInputStream { st ->
			interp.execfile(st)
		}
		interp.set("engine", this)
		
		cre = interp.get("create")
		upd = interp.get("update")
		ren = interp.get("render")
		
		cre.__call__()
	}
	
	void update(float delta){
		pf = new PyFloat(delta)
		upd.__call__(pf)
	}	
	
	void render(){
		ren.__call__()
	}
}
	
