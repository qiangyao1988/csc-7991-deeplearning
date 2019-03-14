//
//  ModelController.swift
//  CoreMLTest
//
//  Created by Kison Ho on 3/14/19.
//  Copyright © 2019 Wayne State University. All rights reserved.
//

import Foundation
import CoreML

// MLViewControllerDelegate interface
protocol MLViewControllerDelegate {
    func showURLError(errorURL: URL) // show an error when cannot get a MLModel for the URL
    func showTestResult() // show the test results
    func showTestError(error: Error) // show test error
}

// Controls MLModel
@available(iOS 12.0, *)
class MLModelController {
    // declare members
//    private var mlFeatureProvider: MLFeatureProvider
    private var mlModel: MLModel?
    private var mlViewControllerDelegate: MLViewControllerDelegate
    
    // constructor
    init(mlModelUrl: URL, mlViewControllerDelegate: MLViewControllerDelegate) {
        // set view controller delegate
        self.mlViewControllerDelegate = mlViewControllerDelegate
        
        // try get ml model
        do {
            self.mlModel = try MLModel(contentsOf: mlModelUrl)
        } catch {
            self.mlViewControllerDelegate.showURLError(errorURL: mlModelUrl)
            self.mlModel = nil
        }
    }
    
    // test model
    func testModel() {
//        do {
//            try self.mlModel?.prediction(from: self)
//        } catch {
//            self.mlViewControllerDelegate.showTestError(error: error)
//        }
    }
}
