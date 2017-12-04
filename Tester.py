from StateMachine import  StateMachine
from GUI import GUI
import sys

class Tester:
    'Class to run the homework assignment using the StateMachine class and GUI class.'

    sm = StateMachine()
    states = {}
    transitions = {}
    accepted = False
    gui = GUI("PL TAKE HOME", 650)  # gui

    def __init__(self):
        self.states = self.sm.getUsedStates()
        self.transitions = self.sm.getUsedTransitions()

    def runAutomata(self, event):
        self.accepted = self.sm.isStringCompatible(self.gui.getEntryText())
        self.states = self.sm.getUsedStates()
        self.transitions = self.sm.getUsedTransitions()
        self.gui.clear()
        self.gui.drawStateMachineOutputLabel(100, 50, "RESULT: " + str(self.accepted))  # DRAW STATE MACHINE OUTPUT
        self.drawStateDiagram()
        return None

    def drawInputControls(self):
        self.gui.drawEntryBox(150, 0, 200)
        self.gui.drawButton(370, 0, 5, 'RUN', self.runAutomata)
        self.gui.clear()
        self.drawStateDiagram()
        self.gui.renderGraphics()

    # DRAW THE MINIMIZED DFA STATE DIAGRAM
    def drawStateDiagram(self):
        dm = 62.5
        rad = dm / 2
        self.gui.drawLabel(75, 15, "ENTER INPUT:", False)
        self.gui.drawState(dm, dm * 4, dm, 'A', False, self.states['A'])  # STATE A
        self.gui.drawState(dm * 3, dm * 4, dm, 'B', False, self.states['B'])  # STATE B
        self.gui.drawState(dm, dm * 6, dm, 'C', False, self.states['C'])  # STATE C
        self.gui.drawState(dm * 5, dm * 4, dm, 'D', False, self.states['D'])  # STATE D
        self.gui.drawState(dm * 3, dm * 6, dm, 'E', False, self.states['E'])  # STATE E
        self.gui.drawState(dm, dm * 8, dm, 'F', False, self.states['F'])  # STATE F
        self.gui.drawState(dm * 5, dm * 2, dm, 'G', False, self.states['G'])  # STATE G
        self.gui.drawState(dm * 3, dm * 8, dm, 'H', True, self.states['H'])  # STATE H
        self.gui.drawState(dm * 7, dm * 2, dm, 'I', True, self.states['I'])  # STATE I
        self.gui.drawTransitionLine(dm * 2, dm * 4 + rad, dm * 3, dm * 4 + rad, self.transitions['A:a'])  # A:a -> B
        self.gui.drawTransitionLine(dm + rad, dm * 5, dm + rad, dm * 6, self.transitions['A:b'])  # A:b -> C
        self.gui.drawTransitionArc(dm * 3 + rad - 10, dm * 3, dm * 3 + rad + 10, dm * 5, 0, 180,
                              self.transitions['B:a'])  # B:a -> B
        self.gui.drawTransitionArc(dm * 4, dm * 4, dm * 5, dm * 4 + rad, 0, 180, self.transitions['B:b'])  # B:b -> D
        self.gui.drawTransitionLine(dm * 2, dm * 6 + rad, dm * 3, dm * 6 + rad, self.transitions['C:a'])  # C:a -> E
        self.gui.drawTransitionLine(dm + rad, dm * 7, dm + rad, dm * 8, self.transitions['C:b'])  # C:b -> F
        self.gui.drawTransitionArc(dm * 4, dm * 4 + rad + 10, dm * 5, dm * 5 + 10, 180, 180, self.transitions['D:a'])  # D:a -> B
        self.gui.drawTransitionLine(dm * 5 + rad, dm * 4, dm * 5 + rad, dm * 3, self.transitions['D:b'])  # D:b -> G
        self.gui.drawTransitionLine(dm * 2, dm * 8 + rad, dm * 3, dm * 8 + rad, self.transitions['F:a'])  # F:a -> H
        self.gui.drawTransitionLine(dm * 2 - 9, dm * 8 + 9, dm * 3 + 9, dm * 7 - 9, self.transitions['F:b'])  # F:b -> E
        self.gui.drawTransitionLine(dm * 6, dm * 2 + rad, dm * 7, dm * 2 + rad, self.transitions['G:a'])  # G:a -> I
        self.gui.drawTransitionArc(dm * 5 + rad - 10, dm, dm * 5 + rad + 10, dm * 3, 0, 180, self.transitions['G:b'])  # G:b -> G
        self.gui.drawTransitionArc(dm * 3, dm * 8 + 20, dm * 5, dm * 9 - 10, 270, 180,
                              self.transitions['H:a'] or self.transitions['H:b'])  # H:a or H:b -> H
        self.gui.drawTransitionArc(dm * 7, dm * 2 + 20, dm * 9, dm * 3 - 10, 270, 180,
                              self.transitions['I:a'] or self.transitions['I:b'])  # I:a or I:b -> I
        self.gui.drawLabel(dm * 2 + rad, dm * 4 + rad - 10, 'a', self.transitions['A:a'])  # A:a
        self.gui.drawLabel(dm + rad + 10, dm * 5 + rad, 'b', self.transitions['A:b'])  # A:b
        self.gui.drawLabel(dm * 3 + rad, dm * 3 - 20, 'a', self.transitions['B:a'])  # B:a
        self.gui.drawLabel(dm * 4 + rad, dm * 3 + rad, 'b', self.transitions['B:b'])  # B:b
        self.gui.drawLabel(dm * 2 + rad, dm * 6 + rad - 10, 'a', self.transitions['C:a'])  # C:a
        self.gui.drawLabel(dm + rad + 10, dm * 7 + rad, 'b', self.transitions['C:b'])  # C:b
        self.gui.drawLabel(dm * 4 + rad, dm * 5 + rad - 10, 'a', self.transitions['D:a'])  # D:a
        self.gui.drawLabel(dm * 5 + rad + 10, dm * 3 + rad, 'b', self.transitions['D:b'])  # D:b
        self.gui.drawLabel(dm * 2 + rad, dm * 8 + rad - 10, 'a', self.transitions['F:a'])  # F:a
        self.gui.drawLabel(dm * 2 + rad + 10, dm * 7 + rad, 'b', self.transitions['F:b'])  # F:b
        self.gui.drawLabel(dm * 6 + rad, dm * 2 + rad - 10, 'a', self.transitions['G:a'])  # G:a
        self.gui.drawLabel(dm * 5 + rad, dm - 20, 'b', self.transitions['G:b'])  # G:b
        self.gui.drawLabel(dm * 5 + rad, dm * 8 + rad, 'a', self.transitions['H:a'])  # H:a
        self.gui.drawLabel(dm * 5 + rad + 20, dm * 8 + rad, 'b', self.transitions['H:b'])  # H:b
        self.gui.drawLabel(dm * 9 + rad, dm * 2 + rad, 'a', self.transitions['I:a'])  # I:a
        self.gui.drawLabel(dm * 9 + rad + 20, dm * 2 + rad, 'b', self.transitions['I:b'])  # I:b
        self.gui.drawPointhead(dm * 5 + 5, dm * 4 + 10, self.transitions['B:b'])
        self.gui.drawPointhead(dm * 4 - 5, dm * 5 - 10, self.transitions['D:a'])

        self.gui.renderGraphics()

    def render(self):
        self.gui.runMainLoop()


tester = Tester()
tester.drawInputControls()
tester.render()
