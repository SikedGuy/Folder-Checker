## un-comment for CLI interface
#from CheckerNoGUI import Checker
#checkerNoGUI = Checker()
#checkerNoGUI.StartSearchNoGUI()
#exit(0)

from CheckerGUI import CheckerWithGUI

checker = CheckerWithGUI()
checker.Run()
