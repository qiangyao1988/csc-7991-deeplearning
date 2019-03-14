//
//  ViewController.swift
//  CoreMLTest
//
//  Created by Kison Ho on 3/14/19.
//  Copyright © 2019 Wayne State University. All rights reserved.
//

import UIKit

// ML View Controller
class MLViewController: UIViewController, MLViewControllerDelegate {
    // declare members
    private var mlModelController: MLModelController?
    
    // declare widgets
    @IBOutlet weak var resultTextView: UITextView!
    @IBOutlet weak var mlProgressView: UIProgressView!
    
    // constructor
    override init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?) {
        super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)
        self.mlModelController = nil
    }
    
    // required constructor
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // show test results
    func showTestResult() {
        
    }
    
    // show test errors
    func showTestError(error: Error) {
        
    }
    
    // show model url error
    func showURLError(errorURL: URL) {
        
    }
    
    // view did load
    override func viewDidLoad() {
        super.viewDidLoad()
        self.mlModelController = MLModelController(mlModelUrl: URL(fileURLWithPath: ""), mlViewControllerDelegate: self)
    }
}

